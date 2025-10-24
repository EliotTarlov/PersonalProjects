pub fn max_product(mut nums: Vec<i32>) -> i64 {
    nums.sort_by(|a, b| b.cmp(a));

    let mut best: i64 = 0;
    for i in 0..nums.len() {
        let limit_64 = best / (nums[i] as i64);
        if limit_64 > (i32::MAX as i64) {
            break;
        }
        let limit = limit_64 as i32;

        if nums[0] <= limit {
            break;
        }

        for j in 0..i {
            if nums[j] <= limit {
                break;
            }
            if nums[i] & nums[j] == 0 {
                best = (nums[i] as i64) * (nums[j] as i64);
                break;
            }
        }
    }

    return best;
}
fn main(){
	println!("{}",max_product((900001..1000001).collect()))
}
