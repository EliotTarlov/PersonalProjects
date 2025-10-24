#include <stdio.h>
#include <vector>
std::vector<int> nums{1,2,3,4,5,6,7};

long long maxProduct(std::vector<int>& nums) {
    long long out=0;
    for(unsigned long i=0; i<nums.size();i++){
        for(unsigned long j=i+1; j<nums.size(); j++){
            long long a=nums[i];
            long long b=nums[j];
            if (not(a&b)){
                if ((a * b) > out){
                     out=a * b;
                }
            }
        }
    }
    return out;
}
int main(){
	printf("%lld",maxProduct(nums));
}
