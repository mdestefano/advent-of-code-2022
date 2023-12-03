use std::fs::File;
use std::fs::read_to_string;

fn main() {
    // read path from command line
    let args: Vec<String> = std::env::args().collect();
    let input_file_path = &args[1];

    solve_part1(input_file_path);
}

fn solve_part1(input_file_path: &String) {
    println!("Solving part 1...");
    println!("Reading input file: {}", input_file_path);

    let lines = read_lines(input_file_path);

    let mut total = 0;
    for line in lines {
        let number = line_to_number(&line);
        total += number;
    }

    println!("Total: {}", total);

}

fn line_to_number(line: &String) -> i32 {
    let (first, last) = find_first_and_last_numeric_chars(line);
    let number = first.to_string() + &last.to_string();
    return number.parse::<i32>().unwrap();
}

fn find_first_and_last_numeric_chars(input: &String) -> (char, char) {
    let first = first_numeric_char(input);
    let last = first_numeric_char(&reverse(input));
    
    return (first, last);
}

fn first_numeric_char(input: &String) -> char {
    for c in input.chars() {
        if c.is_numeric() {
            return c;
        }
    }
    return ' ';
}

fn reverse(input: &String) -> String {
    return input.chars().rev().collect()
}   

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename) 
        .unwrap()  // panic on possible file-reading errors
        .lines()  // split the string into an iterator of string slices
        .map(String::from)  // make each slice into a string
        .collect()  // gather them together into a vector
}


#[cfg(test)]
mod tests {
    use super::*;

    fn test_reverse() {
        let input = String::from("123");
        let oracle = String::from("321");
        assert_eq!(reverse(&input), oracle);
    }

    #[test]
    fn test_first_numeric_char() {
        let input = String::from("abc123");
        let oracle = '1';
        assert_eq!(first_numeric_char(&input), oracle);
    }

    #[test]
    fn test_first_numeric_char_no_numeric() {
        let input = String::from("abc");
        let oracle = ' ';
        assert_eq!(first_numeric_char(&input), oracle);
    }

    #[test]
    fn test_find_first_and_last_numeric_chars() {
        let input = String::from("abc123");
        let oracle = ('1', '3');
        assert_eq!(find_first_and_last_numeric_chars(&input), oracle);
    }

    #[test]
    fn test_line_to_number() {
        let input = String::from("abc123");
        let oracle = 13;
        assert_eq!(line_to_number(&input), oracle);
    }
}
