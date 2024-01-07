use std::{
    error::Error,
    fs::File,
    io::{BufRead, BufReader},
};

use regex::Regex;

#[derive(Debug)]
struct Score {
    red: u32,
    green: u32,
    blue: u32,
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
    id: u32,
    score: Score,
}

impl Game {
    fn parse(line: &String) -> Result<Self, Box<dyn Error>> {
        let id_re = Regex::new("Game (\\d*):")?;
        let id_match = id_re.captures(&line).unwrap().get(1).unwrap();
        let id = id_match.as_str().parse::<u32>()?;

        let scores_re = Regex::new("(\\d*) (red|green|blue)")?;
        let score_captures = scores_re.captures_iter(&line);

        let mut score = Score::new();

        for score_cap in score_captures {
            let count = score_cap.get(1).unwrap().as_str().parse::<u32>()?;
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

        Ok(Self { id, score })
    }

    fn is_valid(&self, best: &Game) -> bool {
        self.score.red <= best.score.red
            && self.score.green <= best.score.green
            && self.score.blue <= best.score.blue
    }
}

pub fn part_one() -> Result<u32, Box<dyn Error>> {
    let file = File::open("src/input/day_two_input.txt").unwrap();
    let lines = BufReader::new(file).lines();

    let mut id_sum: u32 = 0;

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

        let game = Game::parse(&line)?;
        let is_valid = game.is_valid(&best_game);

        if game.is_valid(&best_game) {
            id_sum += game.id;
        }
    }

    println!("Valid Game ID Sum: {}", id_sum);

    Ok(id_sum)
}

pub fn part_two() -> Result<u32, Box<dyn Error>> {
    let file = File::open("src/input/day_two_input.txt").unwrap();
    let lines = BufReader::new(file).lines();

    let mut power_sum: u32 = 0;

    for line in lines {
        let line = line.unwrap();

        let game = Game::parse(&line)?;

        power_sum += game.score.red * game.score.green * game.score.blue
    }

    println!("Game ID Power Sum: {}", power_sum);

    Ok(power_sum)
}
