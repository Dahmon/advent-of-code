use regex::Regex;
use std::fs::File;
use std::io::{self, BufRead, BufReader, Lines};

fn part_one(lines: Lines<BufReader<File>>) -> Result<u32, regex::Error> {
    let first_re = Regex::new(r"^[a-z]*(\d)")?;
    let last_re = Regex::new(r"(\d)[a-z]*$")?;

    let mut total: u32 = 0;

    for line in lines {
        if let Ok(line) = line {
            let first_cap = match first_re.captures(&line) {
                Some(cap) => cap,
                None => continue,
            };
            let last_cap = match last_re.captures(&line) {
                Some(cap) => cap,
                None => continue,
            };

            let first = match first_cap.get(1) {
                Some(first) => first.as_str(),
                None => continue,
            };
            let last = match last_cap.get(1) {
                Some(last) => last.as_str(),
                None => continue,
            };

            let combined = String::from(first) + last;

            total += match combined.parse::<u32>() {
                Ok(total) => total,
                Err(_) => 0,
            };
        }
    }

    Ok(total)
}

fn main() {
    let file = File::open("input.txt").unwrap();

    let lines = io::BufReader::new(file).lines();

    let part_one_result = part_one(lines);
    match part_one_result {
        Ok(result) => println!("Part One Result: {}", result),
        Err(error) => println!("Part One Error: {}", error),
    }
}
