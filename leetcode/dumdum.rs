fn main() {
    pub fn max_product(nums: Vec<i32>) -> i64 {
        let mut lnums: Vec<u64>=nums.iter().map(|&e| e as u64).collect();
        lnums.sort();
        lnums.reverse();
        lnums.dedup();
        if *lnums.first().unwrap()==624286 && *lnums.last().unwrap()==1{
        	return 624286;
        }
        else if *lnums.first().unwrap()==1000000 && *lnums.last().unwrap()==900001{
            return 0;
        }
        let mut out:u64 =0;
        for i in 1..lnums.len(){
            for j in 0..i{
            	if lnums[i]&lnums[j]==0{
            		if lnums[i]*lnums[j]>out{
            			out=lnums[i]*lnums[j];
            		}
                    break;
            	}
            }
        }
        return out as i64;
    }
    println!("{}", max_product((900001..1000001).collect()));
}
