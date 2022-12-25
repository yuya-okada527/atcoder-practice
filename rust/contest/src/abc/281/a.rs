use proconio::input;

fn main() {
    input! {
        mut n: i32,
    }
    loop {
        println!("{}", n);
        n -= 1;
        if n < 0 {
            break;
        }
    }
}
