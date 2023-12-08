use std::str::FromStr;

struct One<'a>(&'a str);
struct Two<'a>(&'a str);

struct Filter {
    start: u32,
    end: u32,
    shift: i32,
}

struct Seed {
    start: u32,
    length: u32
}

impl FromStr for Filter {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut parts = s.split(' ');
        let start = parts.next().unwrap().parse::<u32>().unwrap();
        let end = parts.next().unwrap().parse::<u32>().unwrap() + 1; // +1 to make it inclusive
        let shift = parts.next().unwrap().parse::<i32>().unwrap();

        Ok(Filter { start, end, shift })
    }
}



struct Data {
    seeds: Vec<Seed>,
    filters: Vec<Filter>,
}
