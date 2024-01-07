use std::{
    error::Error,
    fs::File,
    io::{BufRead, BufReader},
};

use regex::Regex;

#[derive(Debug, PartialEq)]
enum Cube {
    Red(u16),
    Green(u16),
    Blue(u16),
}

impl Cube {
    fn from_str(input: &str, value: u16) -> Option<Cube> {
        match input {
            "red" => Some(Cube::Red(value)),
            "green" => Some(Cube::Green(value)),
            "blue" => Some(Cube::Blue(value)),
            _ => None,
        }
    }
}

#[derive(Debug)]
struct Score {
    red: u16,
    green: u16,
    blue: u16,
}

impl Score {
    fn new() -> Self {
        Score {
            red: 0,
            green: 0,
            blue: 0,
        }
    }
}

struct Game {
    id: u16,
    score: Score,
}

impl Game {
    fn is_valid(&self, best: &Game) -> bool {
        self.score.red <= best.score.red
            && self.score.green <= best.score.green
            && self.score.blue <= best.score.blue
    }
}

fn parse_game(line: String) -> Result<Game, Box<dyn Error>> {
    let id_re = Regex::new("Game (\\d*):")?;
    let id_match = id_re.captures(&line).unwrap().get(1).unwrap();
    let id = id_match.as_str().parse::<u16>()?;

    let scores_re = Regex::new("(\\d*) (red|green|blue)")?;
    let score_captures = scores_re.captures_iter(&line);

    let mut score = Score::new();

    for score_cap in score_captures {
        let count = score_cap.get(1).unwrap().as_str().parse::<u16>()?;
        let colour = score_cap.get(2).unwrap().as_str();

        match colour {
            "red" => {
                if count > score.red {
                    score.red = count
                }
            }
            "green" => {
                if count > score.green {
                    score.green = count
                }
            }
            "blue" => {
                if count > score.blue {
                    score.blue = count
                }
            }
            _ => {}
        }
    }

    Ok(Game { id, score })
}

pub fn part_one() -> Result<u16, Box<dyn Error>> {
    let file = File::open("src/day_one_input.txt").unwrap();
    let lines = BufReader::new(file).lines();

    let mut id_sum: u16 = 0;

    let best_game = Game {
        id: 0,
        score: Score {
            red: 12,
            green: 13,
            blue: 14,
        },
    };

    for line in lines {
        let line = line.unwrap();

        let game = parse_game(line)?;
        let is_valid = game.is_valid(&best_game);

        println!("-- Game {} --", game.id);
        println!("{:?}", game.score);
        println!("Is Valid? {}", is_valid);

        if game.is_valid(&best_game) {
            id_sum += game.id;
        }
    }

    println!("Valid Game ID Sum: {}", id_sum);

    Ok(id_sum)
}
