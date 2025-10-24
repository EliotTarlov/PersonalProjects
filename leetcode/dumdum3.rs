
fn main() {
pub fn max_product(nums: Vec<i32>) -> i64 {
    let mut lnums: Vec<u64>=nums.iter().map(|&e| e as u64).collect();
    lnums.sort();
    lnums.reverse();
    let mut out:u64 =0;
    let mut vecs: Vec<Vec<u64>>=Vec::new();
    let mut tmp: Vec<u64>=Vec::new();
    let mut limit=lnums[0].next_power_of_two();
    
    for i in lnums{
        if i<limit{
            while i<limit{
                limit>>=1;
            }
            tmp.push(i);
            vecs.push(tmp.clone());
            tmp.clear()
        }
        else{
            tmp.push(i)
        }
    }
    println!("{}",limit);
    println!("{}",vecs.len());
    for i in 1..vecs.len(){
        for j in 0..i{
        	println!("{},{}",i,j);
            for k in 0..vecs[i].len(){
                for l in 0..vecs[j].len(){
                    if vecs[i][k]*vecs[j][l] < out{
                        break;
                    }
                    if vecs[i][k]&vecs[j][l]==0{
                        out= vecs[i][k]*vecs[j][l];
                        break;
                    }
                }
            }
        }
    
	}
    return out as i64;
}
    println!("{}", max_product((0..500).collect()));
}
