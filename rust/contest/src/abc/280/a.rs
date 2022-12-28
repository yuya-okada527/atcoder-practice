use proconio::input;

fn main() {
    input! {
        t: (i32, i32),
        s: [[String]; t.0]
    }
    dbg!(s);
}
