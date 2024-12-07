use regex::Regex;
use std::fs::File;
use std::io::{self, BufRead};

use crate::ChallengeResult;

pub fn part_one() -> ChallengeResult {
    let file = File::open("src/input/day_one_input.txt").unwrap();
    let lines = io::BufReader::new(file).lines();

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

pub fn part_two() -> ChallengeResult {
    let file = File::open("src/input/day_one_input.txt").unwrap();
    let lines = io::BufReader::new(file).lines();

    let str_nums: [&str; 10] = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ];
    let mut total: u32 = 0;

    for line in lines {
        let line = line.unwrap();
        let mut first: Option<String> = None;
        let mut last: Option<String> = None;

        for (index, char) in line.chars().enumerate() {
            if char.is_digit(10) {
                match first {
                    Some(_) => last = Some(char.to_string()),
                    None => first = Some(char.to_string()),
                }
            }

            for (num_index, str_num) in str_nums.iter().enumerate() {
                if line[index..].starts_with(str_num) {
                    match first {
                        Some(_) => last = Some(num_index.to_string()),
                        None => first = Some(num_index.to_string()),
                    }
                }
            }
        }

        let first = first.unwrap();
        let num: String = match last {
            Some(last) => format!("{}{}", first, last),
            None => format!("{}{}", first, first),
        };

        total += num.parse::<u32>()?;
    }

    Ok(total)
}
