use proconio::input;
use proconio::marker::{Chars};

fn main() {
    input! {
        s: Chars
    }
    let mut ans = 0;
    for c in s {
        if c == 'v' {
            ans += 1;
        } else {
            ans += 2;
        }
    }
    println!("{}", ans);
}
