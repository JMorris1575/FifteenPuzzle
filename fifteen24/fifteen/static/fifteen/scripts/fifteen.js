$(function() {
    const canvas = $("#puzzle-frame")[0];
    const ctx = canvas.getContext('2d');
    const colors = [ ["Crimson", "Red", "DarkRed"], ["Ivory", "White", "AntiqueWhite"] ];

    var request_url = location.pathname

    // Initialization
    start_puzzle(4);

    function start_puzzle(size) {
        $.get(request_url,
            {
                command: 'get_puzzle',
                size: size
            },
            function(data, status) {
                var puzzle_map = data;
                puzzle = new Puzzle(puzzle_map)     // must be inside callback function so it will wait for "get" to finish
                puzzle.draw();
            }
        ); // end of get
    }; // end of get_puzzle

    var puzzle_map = {
        side_tiles: 4,
        start_positions: [15, 6, 10, 0, 2, 4, 8, 12, 14, 5, 11, 9, 13, 3, 7, 1],
        solution: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0],
        style: 'pic'
    }

    var current_pic = new Image();
    current_pic.src = pic_url;
    current_pic.onload = function() {
        let pic = $('#solution-picture');
        pic[0].style.left = (canvas.offsetLeft + 10) + 'px';
        pic[0].style.top = (canvas.offsetTop + 10) + 'px';
        puzzle = new Puzzle(puzzle_map);
        puzzle.draw();
        pic.fadeOut(10000);
    }; // end of current_pic.onload

    class Tile{
        constructor(number, type, image) {
            this.x = -1;        // position will be determined later
            this.y = -1;
            this.dir = null;    // possible direction of motion will be calculated later
            this.number = number;
            this.type = type;
            this.image = image;
        }
        set_position(x, y) {
            this.x = x;
            this.y = y;
        } // end of set_position

        draw_tile(size) {
            if (this.type == 'numeric') {
                var palette = colors[this.number % 2];
                ctx.fillStyle = palette[0];
                ctx.fillRect(this.x, this.y, size, size);
                ctx.globalAlpha = 1;
                ctx.font = size * 0.6 + 'px arial';
                ctx.textBaseline = 'middle';
                ctx.textAlign = 'center';
                var offsetX = this.x + size / 2;
                var offsetY = this.y + size / 2;
                ctx.fillStyle = 'GoldenRod';
                ctx.fillText(this.number.toString(), offsetX, offsetY);
                ctx.strokeStyle = "Grey";
                ctx.strokeText(this.number.toString(), offsetX, offsetY);
            } else {
                if (this.type != 'blank') {
                    ctx.drawImage(this.image, this.x, this.y);
                }
            }// end of Tile.type determination
            if (this.type != 'blank') {
                for (var i=0; i<5; i++) {
                    ctx.beginPath();
                    ctx.moveTo(this.x + i, this.y + size - i);
                    ctx.lineTo(this.x + i, this.y + i);
                    ctx.lineTo(this.x + size - i, this.y + i);
                    ctx.strokeStyle = "rgba(127, 127, 127, " + (1 - (i / 5)) + ")";
                    ctx.stroke()
                }
                for (var i=0; i<5; i++) {
                    ctx.beginPath();
                    ctx.moveTo(this.x + i, this.y + size - i);
                    ctx.lineTo(this.x + size - i, this.y + size - i);
                    ctx.lineTo(this.x + size - i, this.y + i);
                    ctx.strokeStyle = "rgba(0, 0, 0, " + (1 - (i / 5)) + ")";
                    ctx.stroke()
                }
            } // end of type != blank
        } // end of draw_tile()
    } // end of Tile definition

    class Puzzle {
        constructor(puzzle_map) {
            // uses the supplied puzzle_map object to create the current puzzle
            this.side_tiles = puzzle_map['side_tiles'];
            this.size = canvas.height / this.side_tiles;
            this.puzzle_array = [new Tile(0, 'blank', null)]
            var type = puzzle_map['style'];
            for (let i=1; i<this.side_tiles * this.side_tiles; i++) {
                if (type == 'numeric') {
                    var image = null;
                } else {
                    var piece_canvas = document.createElement('canvas');
                    piece_canvas.width = this.size;
                    piece_canvas.height = this.size;
                    var piece_context = piece_canvas.getContext('2d');
                    var row = Math.floor((i - 1)/this.side_tiles);
                    var col = (i - 1) % this.side_tiles;
                    piece_context.drawImage(current_pic, col * this.size, row * this.size, this.size, this.size, 0, 0, this.size, this.size);
                    var image = new Image();
                    image.src = piece_canvas.toDataURL();
                    $('#solution-picture').attr('src', pic_url);
                } // end of style determination
                this.puzzle_array.push(new Tile(i, type, image));
            } // end of filling puzzle_array
            this.grid = [];
            this.solution_grid = [];
            var ptr = 0;
            for (let row=0; row<this.side_tiles; row++) {
                var grid_row_data = [];
                var solution_row_data = [];
                for (let col=0; col<this.side_tiles; col++) {
                    let value = puzzle_map['start_positions'][ptr];
                    grid_row_data.push(value);
                    this.puzzle_array[value].set_position(col * this.size, row * this.size);
                    solution_row_data.push(puzzle_map['solution'][ptr]);
                    ptr++;
                } // end of iteration through the columns
                this.grid.push(grid_row_data);
                this.solution_grid.push(solution_row_data);
            } // end of iteration through the rows
        } // end of Puzzle constructor

        draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (let i=0; i<this.puzzle_array.length; i++) {
                this.puzzle_array[i].draw_tile(this.size);
            } // end of iteration through tiles in puzzle_array
        } // end of draw()

        move(tile_count, rows, cols, dir, blank_row, blank_col) {
            var old_index = 0;
            for (let row_ptr=0; row_ptr<rows.length; row_ptr++) {
                for (let col_ptr=0; col_ptr<cols.length; col_ptr++) {
                    var grid_row = rows[row_ptr];
                    var grid_col = cols[col_ptr];
                    var temp = this.grid[grid_row][grid_col];
                    this.grid[grid_row][grid_col] = old_index;
                    var tile = this.puzzle_array[old_index];
                    tile.set_position(grid_col * this.size, grid_row * this.size);
                    old_index = temp;
                } // end of scan through cols
            } // end of scan through rows
            this.grid[blank_row][blank_col] = old_index;
            tile = this.puzzle_array[old_index];
            tile.set_position(blank_col * this.size, blank_row * this.size);
            one_tile.play();
            this.draw();
            if (JSON.stringify(this.grid) == JSON.stringify(this.solution_grid)) {
                puzzle_solve.play();
                // $('#solution-picture').fadeIn(3000);
            }
        } // end of move()

        process_click(x, y) {
            var col = Math.floor(x / this.size);
            var row = Math.floor(y / this.size);
            var index = this.grid[row][col]
            blank_search: for (var blank_row=0; blank_row<this.side_tiles; blank_row++) {
                for (var blank_col=0; blank_col<this.side_tiles; blank_col++) {
                    if (this.grid[blank_row][blank_col] == 0) { break blank_search; }
                } // end of blank_col for loop
            } // end of blank_search
            if ( ! (row == blank_row && col == blank_col) ) {
                var difference;
                var tile_count;
                var dir;
                var rows = []
                var cols = []
                if (row == blank_row) {
                    difference = blank_col - col;
                    tile_count = Math.abs(difference);
                    dir = difference / tile_count;
                    rows.push(row);
                    for (let i=0; i<tile_count; i++) {
                        cols.push(col + dir * i);
                    } // end of populating columns array
                } // end of row == blank_row
                if (col == blank_col) {
                    difference = blank_row - row;
                    tile_count = Math.abs(difference);
                    dir = difference / tile_count;
                    cols.push(col);
                    for (let i=0; i<tile_count; i++) {
                        rows.push(row + dir * i);
                    } // end of populating rows array
                } // end of col == blank_col
                this.move(tile_count, rows, cols, dir, blank_row, blank_col);
            } // end of blank clicked check
        } // end of process_click()
    } // end of Puzzle class definition

    $('#puzzle-frame').click( function(event) {
        const rect = canvas.getBoundingClientRect();
        mouseX = event.clientX - rect.left - 10; // mouse position adjusted for border width
        mouseY = event.clientY - rect.top - 10;
        if (mouseX >= 0 && mouseX < canvas.width && mouseY >= 0 && mouseY < canvas.height) {
            puzzle.process_click(mouseX, mouseY)
        }
    }); // end of canvas click event listener

    // temporary button listener
    $("button").click( function() {
        start_puzzle(parseInt($(this).text()));
    }); // end of button.click



}); // end ready
