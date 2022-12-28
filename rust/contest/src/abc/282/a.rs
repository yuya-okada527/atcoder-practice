use proconio::input;

fn main() {
    let alphabet = vec![
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ];
    input! {
        mut k: i32,
    }
    for s in alphabet {
        print!("{}", s);
        k -= 1;
        if k == 0 {
            break;
        }
    }
    println!();
}
