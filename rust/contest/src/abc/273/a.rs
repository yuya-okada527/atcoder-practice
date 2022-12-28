use proconio::input;

fn f(k: i32) -> i32 {
    if k == 0 {
        1
    } else {
        k * f(k-1)
    }
}

fn main() {
    input! {
        n: i32
    }
    println!("{}", f(n));
}
