use std::{
    fs::File,
    io::{BufRead, BufReader, Lines},
};

pub struct Input {
    pub lines: Lines<BufReader<File>>,
}

impl Input {
    pub fn open(filename: String) -> Self {
        let file = File::open(filename).unwrap();

        Self {
            lines: BufReader::new(file).lines(),
        }
    }
}
