const GRID_WIDTH:usize=200;
const GRID_HEIGHT:usize =400;
type Grid=[[bool;GRID_WIDTH];GRID_HEIGHT];
use color_eyre::Result;
use crossterm::event::{self, Event};
use ratatui::{DefaultTerminal, Frame};

fn main() -> Result<()>{
	let mut grid:Grid=square_grid();
	color_eyre::install()?;
    let terminal = ratatui::init();
    let result = run(terminal);
    ratatui::restore();
    return result;
    if false{loop{
		print_grid(grid);
		grid=iterate(grid);
	}};
}

fn run(mut terminal: DefaultTerminal) -> Result<()> {
    loop {
        terminal.draw(render)?;
        if matches!(event::read()?, Event::Key(_)) {
            break Ok(());
        }
    }
}

fn render(frame: &mut Frame) {
    frame.render_widget("hello world", frame.area());
}

fn square_grid()->Grid{
	let mut grid=[[false;GRID_WIDTH];GRID_HEIGHT];
	grid[0]=[true;GRID_WIDTH];
	grid[1][100]=true;
	grid[0][10]=false;
	grid
}

fn print_grid(grid:Grid){
	for row in grid.iter() {
	        for &value in row.iter() {
	            print!("{}", if value { '#' } else { ' ' });
	        }
	        println!();
	    }
}
fn iterate(grid:Grid)->Grid{
	let mut new_grid=[[false;GRID_WIDTH];GRID_HEIGHT];
	for y in 1..GRID_HEIGHT-1 {
		let mut new_line=[false;GRID_WIDTH];
		for x in 1.. GRID_WIDTH-1{
			let neighbors=neighbors(grid,x,y);
			if grid[y][x] {
				if  neighbors==3 || neighbors==2{
					new_line[x]=true
				}
			}
			else if neighbors==3{
					new_line[x]=true
			}
		new_grid[y]=new_line
		}
	}
	return new_grid
}
fn neighbors(grid:Grid,x:usize,y:usize)->u8{
	let mut sum=0;
	sum+= grid[y][x-1] as u8;
	sum+= grid[y][x+1] as u8;
	sum+= grid[y+1][x-1] as u8;
	sum+= grid[y+1][x] as u8;
	sum+= grid[y+1][x+1] as u8;
	sum+= grid[y-1][x-1] as u8;
	sum+= grid[y-1][x] as u8;
	sum+= grid[y-1][x+1] as u8;
	return sum;
}
