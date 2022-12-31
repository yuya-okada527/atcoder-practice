use proconio::input;

fn main() {
    input! {
        n: u8,
        a: [i32; n],
    }
    let mut ans = 0;
    for i in a {
        ans += i;
    }
    println!("{}", ans);
}
