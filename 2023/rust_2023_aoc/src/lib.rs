use std::error::Error;

pub mod day_two;

pub fn run() -> Result<(), Box<dyn Error>> {
    day_two::part_one()?;
    day_two::part_two()?;

    Ok(())
}
