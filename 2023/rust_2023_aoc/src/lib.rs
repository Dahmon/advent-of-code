use std::error::Error;

pub mod day_one;

pub fn run() -> Result<(), Box<dyn Error>> {
    day_one::part_one();

    Ok(())
}
