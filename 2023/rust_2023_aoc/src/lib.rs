use std::error::Error;

pub mod day_one;
pub mod day_three;
pub mod day_two;

// pub mod utils;

pub fn run() -> Result<(), Box<dyn Error>> {
    match day_one::part_one() {
        Ok(result) => println!("Part One Result: {}", result),
        Err(error) => println!("Part One Error: {}", error),
    }
    match day_one::part_two() {
        Ok(result) => println!("Part Two Result: {}", result),
        Err(error) => println!("Part Two Error: {}", error),
    }

    day_two::part_one()?;
    day_two::part_two()?;

    Ok(())
}
