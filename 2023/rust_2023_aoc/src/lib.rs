use std::error::Error;

pub mod day_one;
pub mod day_three;
pub mod day_two;

pub mod utils;

pub type ChallengeResult = Result<u32, Box<dyn Error>>;

pub fn run() -> Result<(), Box<dyn Error>> {
    // for (part_one, part_two) in &[
    //     (&day_one::part_one, &day_one::part_two),
    //     (&day_two::part_one, &day_two::part_two),
    // ] {
    //     match part_one() {
    //         Ok(result) => println!("Part One Result: {}", result),
    //         Err(error) => println!("Part One Error: {}", error),
    //     }

    //     match part_two() {
    //         Ok(result) => println!("Part Two Result: {}", result),
    //         Err(error) => println!("Part Two Error: {}", error),
    //     }
    // }

    day_one::part_one()?;
    day_one::part_two()?;

    day_two::part_one()?;
    day_two::part_two()?;

    day_three::part_one()?;

    Ok(())
}
