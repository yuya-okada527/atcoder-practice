use proconio::input;
use proconio::marker::{Chars};

fn main() {
    input! {
        s: Chars
    }
    let mut ans = -1;
    let mut count = 1;
    for i in s {
        if i == 'a' {
            ans = count;
        }
        count += 1;
    }
    println!("{}", ans);
}
