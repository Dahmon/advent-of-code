use crate::{utils::Input, ChallengeResult};

// Part One Ideas:
// Create a mask of symbol effective areas + each number.
// Any overlap indicates the number is a valid part number.
// - This works, but not ideal. Creating mask for each number seems convoluted and slow.
//
// Create a mask of symbols only, with a method for finding if given point is near a symbol.

#[derive(Debug)]
struct SymbolMask {
    mask: Vec<Vec<bool>>,
}

impl SymbolMask {
    fn build(input: Input) -> Self {
        let mut mask = vec![vec![]];

        for (line_index, line) in input.lines.enumerate() {
            if line_index > mask.len() {
                continue;
            };

            for (char_index, char) in line.unwrap().chars().enumerate() {
                match char {
                    '@' | '#' | '$' | '%' | '&' | '+' | '=' | '/' => {
                        mask[line_index][char_index] = true
                    }
                    _ => (),
                };
            }
        }

        Self { mask }
    }

    fn is_near(&self, row: u16, column: u16) -> bool {
        false
    }
}

pub fn part_one() -> ChallengeResult {
    let input = Input::open("src/input/day_three_input.txt".to_string());
    // let lines: Vec<_> = input.lines.collect();
    // let chars: Vec<Vec<char>> = lines
    //     .into_iter()
    //     .map(|l| l.unwrap().chars().collect())
    //     .collect();

    let symbol_mask = SymbolMask::build(input);

    println!("{:?}", symbol_mask);
    println!("{:?}", symbol_mask.mask);

    // for char, if numeroc, call is_near
    Ok(0)
}
