use proconio::input;

fn main() {
    input! {
        a: i32,
        b: i32,
    }
    let mut ans = 1;
    for _ in 0..b {
        ans *= a;
    }
    println!("{}", ans);
}
