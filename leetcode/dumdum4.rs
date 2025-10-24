
fn main() {

pub fn max_product(nums: Vec<i32>) -> i64 {
    let mut lnums: Vec<u64>=nums.iter().map(|&e| e as u64).collect();
    lnums.sort();
    lnums.reverse();
    let mut max=0;
    let mut maximum_of_each_order: Vec<u64>=Vec::new();
    let mut highest_order=lnums[0].next_power_of_two();
    for i in 0..lnums.len(){
    	println!("{},{:b},{},{}",lnums[i],lnums[i],highest_order,lnums[i]&highest_order);
        if lnums[i]&highest_order == 0 || lnums[i]==highest_order{
            while lnums[i]&highest_order == 0{
                if highest_order==0{
                    panic!();
                }
    			//println!("{},{},{},{}",i,lnums[i],highest_order,lnums[i]&highest_order);
                highest_order>>=1;
            }
            maximum_of_each_order.push(lnums[i]);
        }
    }
    println!("{:#?}",maximum_of_each_order);
    for i in &maximum_of_each_order{
        for j in &lnums{
            if i&j==0{
                if i*j>max{
                    max=i*j;
                }
            }
        }
    }
    return max as i64
}
	println!("{}", max_product([14,12,20,2,19].to_vec()));
}
