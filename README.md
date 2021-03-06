# SwordTarget-OFFER
## 剑指OFFER的题目
### 按难度顺序查看：[简单](#简单)、[中等](#中等)、[较难](#较难)<br>
### 按分类查看：[数组](#数组)、[树](#树)、[字符串](#字符串)、[数学](#数学)、[链表](#链表)、[贪心](#贪心)、[排序](#排序)、[哈希](#哈希)、[位运算符](#位运算符)、[二分搜索](#二分搜索)、[动态规划法](#动态规划法)、[场景模拟法](#场景模拟法)<br>

### 简单：<br>
1.[二叉树的深度](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%B7%B1%E5%BA%A6.py)<br>
直接思路:递归把每个子树的高度都算出来，递归停止条件是空树，递归返回是max{左子树高度，右子树高度}+1(当前层)。运行时间23ms,占用内存5752K。<br>
参考思路:或者借助队列使用层次遍历方法，在开始时记录队列长度，然后将这个长度的个数的元素依次出队列，出队时如果此结点还有左右子树，那么将其左右子树入队。在队列长度个元素出队之后，树的高度+1。运行时间46ms,占用内存5736K<br>
2.[不用加减乘除运算符做加法](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%B8%8D%E7%94%A8%E5%8A%A0%E5%87%8F%E4%B9%98%E9%99%A4%E5%81%9A%E5%8A%A0%E6%B3%95.py)<br>
直接思路:转换成列表型的二进制，然后用if判断来模拟手算二进制的情况，重点在于要补位。（此方法提交时内存溢出）<br>
参考思路:使用位运算符进行操作，两数异或后在左移一位取得进位。值得注意的是，此方法对于C/JAVA来说即使遇到异号数相加大于0的情况也最终会溢出并计算出正确结果，但是python是没有位数限制的，会不断无限的迭代至负无穷，所以对于此类情况应该反着来计算，并将最后结果取反。运行时间20ms，占用内存5860K<br>
3.[构建乘积数组](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%9E%84%E5%BB%BA%E4%B9%98%E7%A7%AF%E6%95%B0%E7%BB%84.py)<br>
直接思路:使用双重循环直接实现。外层循环是传入的列表的长度，内层循环是列表中元素的乘积，遇到索引相同的则跳过这次循环。运行时间33ms，占用内存5716K<br>
参考思路:经过分析可以发现，B[i]=C[i]\*D[i],其中C[i]=A[0]\*A[1]*...*A[i-1]，D[i]=A[i+1]*...*A[n],则不难发现C[i]=C[i-1]*A\[i-1\](i=1,2...n),C[0]=1。D[i]=D[i+1]*A\[i+1\](i=0,1...n-1)，D[n]=1。有此规律，直接使用两个for循环计算出C和D数组。运行时间27ms，占用内存5816K<br>
4.[变态台阶跳](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%8F%98%E6%80%81%E8%B7%B3%E5%8F%B0%E9%98%B6.py)<br>
直接思路:通过数学归纳法可以得到n台阶有的跳法为2^(n-1)。则可以直接得到结果。运行时间32 ms，占用内存5840K。<br>
参考思路:设n级台阶能够有的跳法数为f[n]，则很显然f[n]=f[n-1]+f[n-2]+...+f[0]（上一层在n-1层再跳1层+上一层在n-2层再跳2层...上一层没有再跳n层）。运行时间26ms，占用内存5860K<br>
5.[二叉树的镜像](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%95%9C%E5%83%8F.py)<br>
直接思路:使用递归方法不断交换节点的左右子树。运行时间22ms,占用内存5876K。<br>
间接思路:消去递归，使用堆栈，将根节点压入栈中，然后开始循环：若栈不空，出栈一个元素，并交换其左右节点，然后再将其左右节点入栈。否则结束。运行时间21ms，占用内存5736K。<br>

### 中等：<br>
1.[重建二叉树](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E9%87%8D%E5%BB%BA%E4%BA%8C%E5%8F%89%E6%A0%91.py)<br>
直接思路:先序-》第一个是根节点-》中序中寻找到这个根节点，然后将左右切分，左边的结点个数就是根节点左子树的结点个数。去先序接着根找依次这个个数的片段，找到后，又第一个是根节点，以此类推。运行时间66ms，占用内存5984K<br>
2.[剪绳子](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%89%AA%E7%BB%B3%E5%AD%90.py)<br>
思路：设长度为n的绳子剪成起码两段以上的绳子的乘积最大值为f(n)，则易知f(n)=max{1\*f(n-1),2\*f(n-2),...,(n-1)\*f(1)}。而且f(n)起码会切分成两段，而长度为4以下的绳子再切都不可能比原来大，所以长度4以下的绳子需要分类讨论。而大于5长度的绳子f(1)=1,f(2)=2,f(3)=3,f(4)=4。运行时间33ms,占用内存6120K<br>
3.[数据流中的中位数](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%95%B0%E6%8D%AE%E6%B5%81%E7%9A%84%E4%B8%AD%E4%BD%8D%E6%95%B0.py)<br>
直接思路:每输入一个就排序一次，那么奇数列表的中位数就是中间那个数，偶数列表的中位数就是中间两个数之和。运行时间20ms,占用内存5732K<br>
参考思路:利用最大堆和最小堆来实现，将一个数据流的有序排列看作是两个堆的存储。如\[1,2,3,4,5,6\],那么左边1,2,3存储在最大堆中，右边4,5,6存储在最小堆中。那么很显然这个列表的中位数就是最大堆的堆顶元素和最小堆的堆顶元素之和除以2。而如\[1,2,3,4,5\]，那么左边1,2,3存储在最大堆中，右边4,5存储在最小堆中，此时中位数就是最大堆的堆顶元素。那么只要每次把插入的元素，流走于两个堆之间，找到相应的位置，然后再设法将两个堆的元素个数规范，那么中位数就可容易得出。运行时间28ms,占用内存5720K<br>
4.[把二叉树打印成多行](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%8A%8A%E4%BA%8C%E5%8F%89%E6%A0%91%E6%89%93%E5%8D%B0%E6%88%90%E5%A4%9A%E8%A1%8C.py)<br>
直接思路:用队列和计数器解决，当计数器为0时，说明要开始新的一层了，将计数器置为当前队列长度，每出队一个元素，计数器减一。然后若出队结点的左右子树存在，则将其入队。不断循环这个过程，直到队列为空结束。运行时间30ms,占用内存5832k<br>
间接思路:将直接思路中的计数器用while循环代替优化。然后发现这其实是Bfs的变例。运行时间22ms，占用内存5728k<br>
5.[二叉树的下一个结点](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E4%B8%8B%E4%B8%80%E4%B8%AA%E7%BB%93%E7%82%B9.py)<br>
直接思路:首先将所给结点不断找父节点，直到找到根节点，然后对根节点使用递归中序遍历，然后将中序遍历的结果保存，然后返回定结点的下一个结点就好了。运行时间22ms,占用内存5860k<br>
6.[链表中环的入口结点](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%8E%AF%E7%9A%84%E5%85%A5%E5%8F%A3%E7%BB%93%E7%82%B9.py)<br>
直接思路:首先把遍历的结点保存在列表中（最好是哈希表其实，这样更快，但是我没有用哈希表）。然后判断新遍历的结点是否存在于列表中，若存在，则直接返回当前结点。否则当所有结点遍历完毕后返回None。运行时间29ms，占用内存5860k<br>
7.[字符流中第一个不重复的字符](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%AD%97%E7%AC%A6%E6%B5%81%E4%B8%AD%E7%AC%AC%E4%B8%80%E4%B8%AA%E4%B8%8D%E9%87%8D%E5%A4%8D%E7%9A%84%E5%AD%97%E7%AC%A6.py)<br>
直接思路:首先创建一个字典，用于记录字符出现的次数。再创建一个列表，用于记录插入的字符。若插入的字符在字典中不存在，则在字典中创建新的字符索引并记录值为1，否则对应索引的记录值加1。最后遍历列表，每个元素对应字典中索引中若有记录值为1的，则直接返回这个元素。若列表遍历完毕还没有返回，则返回#。运行时间21ms，占用内存5732k<br>
8.[表示数值的字符串](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E8%A1%A8%E7%A4%BA%E6%95%B0%E5%80%BC%E7%9A%84%E5%AD%97%E7%AC%A6%E4%B8%B2.py)<br>
直接思路:没什么花里胡哨的，直接使用正则匹配，若正则匹配后的结果和原来的结果一样，则返回True，否则返回False。运行时间22ms,占用内存5720k<br>
9.[数组中重复的数字](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%95%B0%E7%BB%84%E4%B8%AD%E9%87%8D%E5%A4%8D%E7%9A%84%E6%95%B0%E5%AD%97.py)<br>
直接思路:直接把给进的数字列表当队列，出队一个元素后判断元素是否在队列里，如果在，则表示这个元素重复，返回True，要是队列全部元素都出队了，返回False。运行时间22ms,占用内存5852k<br>
间接思路:因为给定的数组里的数字不会大于数组长度-1，所以对于没有重复元素的数组来说，必定是有0\~数组长度-1的数在数组里。所以从下标0开始，将里面的元素和这个元素下标的值进行交换，直到遇见相等的时候表示这个元素重复了。否则就一直交换，直到下标和这个下标对应的数组元素相等时，再对下一个下标重复此操作。如果最后操作完了所有下标，则返回False。运行时间21ms，占用内存5732k<br>
10.[求1+2+...+n](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%B1%821%2B2...%2Bn.py)<br>
直接思路:使用递归加来代替循环。利用and的短路原理来实现递归的终止。运行时间31ms,占用内存5752k<br>
11.[圆圈中最后剩下的数](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%9C%86%E5%9C%88%E4%B8%AD%E6%9C%80%E5%90%8E%E5%89%A9%E4%B8%8B%E7%9A%84%E6%95%B0.py)<br>
直接思路:第一次报数的时候，去掉的是下标为(m-1)%n的小朋友。第二次报数的时候，去掉的是((m-1)%n+m-1)%(n-1)下标的小朋友。所以，易得，设第n次报数去掉的小朋友下标为f\[n\]。则易知f\[1\]=(m-1)%n，f\[2\]=(f\[1\]+m-1)%(n-2)......f\[n-2\]=(f\[n-3\]+m-1)%2。所以，直接用一个列表存储0\~n-1代表n个小朋友。每k次去掉下标为f\[k\]的元素。这样，等到列表只剩1个元素的时候，那个就是剩下来的小朋友。运行时间23ms，占用内存5708k<br>
12.[扑克牌顺子](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%89%91%E5%85%8B%E7%89%8C%E9%A1%BA%E5%AD%90.py)<br>
直接思路:首先对列表进行排序，然后遍历到第一个不为0的数的下标i。将flag视为i。然后将下标为i的元素与下标i以后的元素逐个比对，如果有相同元素，直接返回false，如果下标为i的元素与后面的元素的差的绝对值大于等于0以外的数个数，那么flag的值减去超出的部分并重新赋值给flag。如果遍历结束后。flag等于0，则返回True，否则返回False。运行时间23ms,占用内存5752k<br>
改进思路:其实不用这么复杂，无论有多少个0，都必须满足最小的那个非0值减去最大的值的绝对值要小于5就可以了。所以只需要排序后，判断最大的值减最小的值的差是否小于5，若小于5则返回True，否则返回False。运行时间21ms，占用内存5624k<br>
13.[左旋字符串](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%B7%A6%E6%97%8B%E5%AD%97%E7%AC%A6%E4%B8%B2.py)<br>
直接思路:使用队列，将字符串的字符存入队列中，然后循环n次，出队入队。运行时间32ms,占用内存5752k<br>
间接思路:直接使用字符串切片操作，将字符串切成\[0:n\]的部分和\[n:end\]的部分。然后组合的时候颠倒一下次序。运行时间22ms,占用内存5736k<br>
14.[和为S的两个数字](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%92%8C%E4%B8%BAS%E7%9A%84%E4%B8%A4%E4%B8%AA%E6%95%B0%E5%AD%97.py)<br>
直接思路:从头开始遍历，遇到和大于给定目标值的则直接break，否则如果和等于目标值，则返回这两个值。因为是从头开始遍历的，所以肯定是乘积最小的那组和。运行时间27ms,占用内存5752k<br>
间接思路:哈希法，由于若A+B=SUM，则B=SUM-A，所以先把列表中的值存入字典，然后通过遍历列表，判断SUM-遍历的值是否在字典中，如果在，则判断其乘积是否小而暂存这两个数。最后返回的两个数肯定是最小的。运行时间22ms,占用内存5948k<br>
15.[和为S的连续正数序列](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%92%8C%E4%B8%BAS%E7%9A%84%E8%BF%9E%E7%BB%AD%E6%AD%A3%E6%95%B0%E5%BA%8F%E5%88%97.py)<br>
直接思路:用i遍历tsum以内的数字，再嵌套用j遍历i以后到tsum的数字，直到i到j的和大于tsum为止。把i到j的和求出来，同时记录下i到j的数字，如果等于tsum，则这组数字即为一个答案。跳出j遍历的循环。运行时间23ms,占用内存5752k<br>
间接思路:数学法。<br>
由于连续数字的和可以用公式来计算，设首项为x，末项为y，则其和为(x+y)\*(y-x+1)\/2。即y^2+y-x^2+x-2\*tsum=0。则可以计算出y=(-1+sqrt(1-4*(-x^2+x-2\*tsum)))/2。若y为整数，则说明x到y则为答案。所以将x从1到tsum进行遍历，计算y的值，若y为整数，则即为一个答案。运行时间22ms,占用内存5624k<br>
16.[数组中只出现一次的数字](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%95%B0%E7%BB%84%E4%B8%AD%E5%8F%AA%E5%87%BA%E7%8E%B0%E4%B8%80%E6%AC%A1%E7%9A%84%E6%95%B0%E5%AD%97.py)<br>
直接思路:对列表进行出栈pop操作，然后判断若这个元素存在于列表中，则直接remove这个元素。否则将其加入答案列表，若答案列表中元素有两个，则返回答案列表。运行时间28ms,占用内存5644k<br>
改进思路:由于remove操作的时间复杂度依然会是O(n)，所以多用一个字典存储出栈后的元素，出栈元素不存在于字典的键中，则创建一个这个元素的键，并将其值设为1。判断出栈元素是否在列表中，若存在，则对应键的值+1，否则判断该键对应的值是否为1，若为1则存入答案列表，若答案列表长度是2，直接返回答案列表。运行时间21ms,占用内存5732k<br>
17.[平衡二叉树](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.py)<br>
直接思路:先用递归写一个获得树高度的函数，然后遍历所有节点，判断其左右子树高度差的绝对值是否大于1，如果大于1则不是二叉平衡树，所有节点遍历完了以后还没返回False，就说明是二叉平衡树。运行时间24ms,占用内存5876k<br>
改进思路:遍历节点的时候可以使用后序遍历法，这样先判断子树满不满足二叉平衡树的条件，如果满足，则继续遍历，否则直接返回False，不需要再判断其根节点了。运行时间25ms,占用内存5636k<br>
18.[数字在排序数组中出现的次数](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%95%B0%E5%AD%97%E5%9C%A8%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E5%87%BA%E7%8E%B0%E7%9A%84%E6%AC%A1%E6%95%B0.py)<br>
直接思路:利用一次循环遍历列表，判断相等的目标元素的个数。如果遇到大于目标元素的值，则break。运行时间21ms,占用内存5728k<br>
间接思路:二分搜索法寻找目标元素的边界。上界为使用二分搜索法寻找到第一个大于目标元素值的索引，下界为使用二分搜索法寻找到第一个等于目标元素值的索引，如果目标元素不存在于列表中，则下界肯定只能寻得第一个大于目标元素值的索引。最终的目标元素出现次数为上界减去下界。运行时间17ms,占用内存5752k<br>
19.[两个链表的第一个公共结点](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%B8%A4%E4%B8%AA%E9%93%BE%E8%A1%A8%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%85%AC%E5%85%B1%E7%BB%93%E7%82%B9.py)<br>
直接思路:两个循环两个指针，从头开始遍历，然后判断是否两个指针指向的结点是否相同。如果相同则返回任意一个指针，否则继续。遍历结束返回空。运行时间18ms,占用内存5764k<br>
间接思路:由于两个链表长度的和是一样的，所以将两个链表拼接起来。到达相同结点的长度肯定是一样的，那么只需要遍历一次，两个指针跟着移动，如果到底了就拼接起来，否则就继续移动，直到找到相同的结点退出循环，并返回那个结点。如果没有公共结点的话，拼起来长度一样，最终都会到两个None，此时也算是相等的结点，刚好返回None。运行时间18ms,占用内存5752k<br>
20.[整数中1的出现次数\(从1到n整数出现的次数\)](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%95%B4%E6%95%B0%E4%B8%AD1%E5%87%BA%E7%8E%B0%E7%9A%84%E6%AC%A1%E6%95%B0(%E4%BB%8E1%E5%88%B0n%E6%95%B4%E6%95%B0%E5%87%BA%E7%8E%B0%E7%9A%84%E6%AC%A1%E6%95%B0).py)<br>
直接思路:想总结出数学规律，但是失败了。<br>
间接思路:暴力循环。初始化计数器为0，从1到n开始遍历，每个数通过循环取余的方法判断个、十、百。。。位是否为1，然后每有一个位为1，计数器就加1。最后计数器的值就是答案。运行时间37ms,占用内存5740k<br>
21.[连续子数组的最大和](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E8%BF%9E%E7%BB%AD%E5%AD%90%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E5%A4%A7%E5%92%8C.py)<br>
直接思路:遍历数组所有数，每一个再嵌套循环遍历他后面的数的和，并将所有的和存入列表中，最后返回列表中的最大值。运行时间18ms,占用内存5740k<br>
间接思路:动态规划法。设结尾是第i个元素的最长连续子数组最大值为dp\[i\]，则dp\[i\]=max{dp\[i-1\]+array\[i-1\],array\[i-1\]}，因为在数组array中第i个元素是array\[i-1\]。所以从dp\[0\]=0开始遍历到最后。并且最好每次都判断出dp几最大，然后返回最大值。运行时间18ms,占用内存5748k<br>
22.[数组中出现次数超过一半的数字](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%95%B0%E7%BB%84%E4%B8%AD%E5%87%BA%E7%8E%B0%E6%AC%A1%E6%95%B0%E8%B6%85%E8%BF%87%E4%B8%80%E5%8D%8A%E7%9A%84%E6%95%B0%E5%AD%97.py)<br>
直接思路:哈希法，构建一个哈希表，遍历一遍数组，如果遍历到的元素存在于哈希表，则对应的哈希值+1，并判断此哈希值是否超过了数组长度的一半，如果是则返回此值。若遍历到的元素不存在于哈希表内，则创建对应的哈希键值并赋值为1。遍历完数组后返回0。运行时间18ms，占用内存5728k<br>
间接思路:候选法，由于众数肯定是超过数组中的一半的那个数，所以将数组中两个不相等的元素相互抵消，这样每次最差的结果就是抵消了一个众数和一个非众数，最终保留在数组中的一定是众数。所以创建一个候选人模型，遍历过程中用一个选票值变量cnt记录当前候选数cond所有的次数，当cnt为0的时候，说明该值已经被抵消过了，取当前遍历的这个值重新做候选数，并让其cnt+1。若cnt不为0，则说明候选数当前没有抵消完，判断候选数与当前遍历到的元素是否相等，如果相等则cnt+1，否则就和当前元素抵消掉，cnt-1。最后保留的那个候选数，再判断它在数组中出现次数是否大于数组一半。运行时间18ms,占用内存5796k<br>
23.[二叉搜索树与双向链表](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%8E%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8.py)<br>
直接思路:中序遍历整颗树，将结点存入列表中。然后整个列表是有序的，直接把列表遍历一遍从头到尾连起来就成了有序的双向链表。运行时间27ms，占用内存5752k<br>
24.[栈的压入、弹出序列](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%A0%88%E7%9A%84%E5%8E%8B%E5%85%A5%E3%80%81%E5%BC%B9%E5%87%BA%E5%BA%8F%E5%88%97.py)<br>
直接思路:本来想着找出什么规律，但是根本没有发现规律。<br>
间接思路:模拟法，根据输出的序列，模拟入栈，如果最终可以成功将栈清空，则说明输出序列可行，否则不可行。具体做法是：利用两个指针p1,p2分别指向输入和输出的序列首端。直到两个指针超界前循环判断p1所指元素是否等于p2所指元素，如果不等，则将p1指向元素压入栈中，并且p1指向下一个元素。如果相等，则说明入栈马上出栈，则直接p1和p2指向下一个元素，此时直到p2指向元素不等于栈顶元素，循环出栈栈顶元素。最终全部循环结束后，若栈为空，则说明输出序列可能，返回True，否则返回False。运行时间19ms，占用内存5752k<br>
25.[合并两个排序的链表](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%8E%92%E5%BA%8F%E7%9A%84%E9%93%BE%E8%A1%A8.py)<br>
直接思路:用两个指针指向两个链表的头，然后新创一个链表，判断指针指向的链表的值哪个小，把小的连到新的链表中去，然后对应的那个指针指向下一个元素，直到有某个链表的指针指向了空为止，然后将另一个链表指针后的所有元素再连在新的链表后面。运行时间19ms，占用内存5624k<br>
间接思路:使用递归的方法来实现上述的思路，可以直接用两个链表不停递归连接。但是效率没有直接思路的高。运行时间22ms，占用内存5688k<br>
26.[反转链表](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.py)<br>
直接思路:头插法，从头到尾遍历单链表，新建一个新的单链表节点，不断将遍历到的节点按头插的形式插入新的链表中，即可完成链表的反转。运行时间19ms,占用内存5624k<br>
27.[数值的整数次方](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%95%B0%E5%80%BC%E7%9A%84%E6%95%B4%E6%95%B0%E6%AC%A1%E6%96%B9.py)<br>
直接思路:调用pow函数。省时省力。运行时间20ms，占用内存5692k<br>
间接思路:分成幂指数大于0，小于0和等于0的情况，大于0时则直接使用for循环乘幂指数次，小于0时则把数值取倒数，然后再for循环乘幂指数次，等于0则直接返回1。运行时间22ms,占用内存5720k<br>
28.[二进制中1的个数](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E8%BF%9B%E5%88%B6%E4%B8%AD1%E7%9A%84%E4%B8%AA%E6%95%B0.py)<br>
直接思路:正数好办，直接辗转相除法，然后判断每次余数是否等于1，等于1就计数。对于负数，由于剑指上使用的是32位的数，但是python是无限位数的。所以首先把负数变成正数，然后开始辗转相除法，并且每次取余数的时候，要取反码。使用两个标记flag和bin_count记录当前情况，flag=1表示已经解决完补码+1的问题了，剩下的直接判断反码是1还是0就可以了，flag=2表示补码+1的进位还在，此时遇到余数为1要继续进位，直到余数为0或者超32位为止。bin_count用于记录当前是多少位了，少于32位循环将继续下去，并且每次都是余数视为1。运行时间19ms，占用内存5748k<br>
间接思路:发现有val :1101000, val-1: 1100111 那么val & （val-1） : 1100000的规律，那么每次遇到一个1，都可以通过val&val-1的方式去消除那个1。所以只需要在给定的数n不为0且n>=-2147483648(32位的最小值)的时候，不断循环计数+1，n=n&(n-1)。运行时间18ms,占用内存5748k<br>
29.[矩形覆盖](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E7%9F%A9%E5%BD%A2%E8%A6%86%E7%9B%96.py)<br>
直接思路：通过人工计算前4个矩形的覆盖方法数可得，假设用n个2\*1的矩形覆盖一个2\*n的矩形的方法数为f\[n\]，则f\[n\]=f\[n-1\]+f\[n-2\]。那么根据递推的规则，很容易想到动态规划法，使用动态规划法进行递推计算，得到f\[n\]。运行时间26ms,占用内存5684k<br>
30.[跳台阶](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E8%B7%B3%E5%8F%B0%E9%98%B6.py)<br>
直接思路：很容易就能想到，台阶为n的情况下，可以是台阶n-1的基础上跳1台阶跳上来，也可以是台阶n-2的基础上跳2台阶跳上来，所以很显然假设跳n台阶的跳法为f\[n\]，且f\[n\]=f\[n-1\]+f\[n-2\]。可以利用动态规划法递推计算出来。运行时间18ms,占用内存5744k<br>
31.[斐波那契数列](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97.py)<br>
直接思路：动态规划法的例子，本身斐波那契数列就是递推式，直接递推计算即可。运行时间16ms,占用内存5744k<br>
32.[旋转数组的最小数字](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%97%8B%E8%BD%AC%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E5%B0%8F%E6%95%B0%E5%AD%97.py)<br>
直接思路:由于旋转后的数组必然出现断崖式的值变化，而且在出现变化前都是单调不减的，所以只需要遍历判断前一个元素比后一个元素大的时候返回那个后一个元素。然后如果遍历完整个数组都不存在前一个元素比后一个元素大，则返回数组\[0\]。运行时间482ms,占用内存5748k，在LeetCode中执行时间44ms，击败45.82%用户，占用内存13.9MB，击败9.23%的用户<br>
间接思路:利用二分搜索的方法对数组进行搜索，首先要解决的就是比较元素的选取问题，这里我们取中间值，然后与两个边界值进行比较，如果中间值比左边界的元素大，则左边界变成mid+1，因为说明前面还是增，否则就判断中间值元素是否比右边界小，如果比右边界小，说明右边区域是单增的，所以右边界变为中间值，如果既不比左边界值大，又不比右边界小，则左边界+1。运行时间513ms,占用内存5748k,在LeetCode中执行时间32ms，击败96.9%用户，内存消耗13.8MB，击败24.62%用户。<br>

### 较难：<br>
1.[二维数组查找](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E6%9F%A5%E6%89%BE.py)<br>
直接思路：将二维数组每一行当做一个数组。然后分别对其进行对半搜索，搜索到则停。时间复杂度大概为O（nlogm），n为二维数组行数，m为二维数组列数。运行时间221 ms，占用内存5732K<br>
参考答案思路：由于二维数组左下角的元素是这一行的最小元素，同时也是这一列的最大元素，那么从这个位置开始对比，若目标元素大则往右走，若目标元素小则往左走。运行时间205 ms，占用内存5852K<br>
2.[替换空格](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%9B%BF%E6%8D%A2%E7%A9%BA%E6%A0%BC.py)<br>
直接思路:将字符串以" "为分割点分割。然后再用"20%"组合起来。运行时间32 ms，占用内存5724K<br>
参考思路:直接使用replace方法将" "替换成"20%"。运行时间23 ms，占用内存5752K<br>
不使用函数自己写的思路:遍历一遍字符串，同时生成一个新的字符串，遍历到空格的时候生成字符串的时候生成"%20"。运行时间24ms，占用内存5860K<br>
3.[从尾到头打印链表](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BB%8E%E5%B0%BE%E5%88%B0%E5%A4%B4%E6%89%93%E5%8D%B0%E9%93%BE%E8%A1%A8.py)<br>
直接思路:和链表逆置挺像的，头插法插入列表里。如果没有insert方法的话。用堆栈放进去再弹出来。运行时间30 ms，占用内存5728K<br>
4.[二叉搜索树的第k个结点(java、python双版本代码)](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E7%AC%ACk%E4%B8%AA%E7%BB%93%E7%82%B9.py)<br>
直接思路:使用中序遍历将二叉搜索树遍历完了以后得到的列表就是一个有序的列表，只需要取出第k个元素就为结果。运行时间34ms,占用内存5744k<br>
间接思路:但是我们其实只需要第k的结点而已，直接思路的方法却存了一堆没用的结点。所以在使用中序遍历的时候，不将遍历结果存储下来，设置一个计数器，当计数器达到了k的时候，将那个元素返回。运行时间19ms,占用内存5624k<br>
5.[链表中倒数第k个结点(java、python双版本代码)](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E9%93%BE%E8%A1%A8%E4%B8%AD%E5%80%92%E6%95%B0%E7%AC%ACk%E4%B8%AA%E7%BB%93%E7%82%B9.py)<br>
直接思路:设计一个大小为k的滑动窗口，将两个距离为k-1的指针p1,p2指向链表中的第1个结点和第k个结点，然后同时移动p1和p2，直到p2.next为空为止，则此时p1所指向的结点即为倒数第k个结点。运行时间26ms，占用内存6520k<br>
6.[二叉树中和为某一值的路径(java、python双版本代码)](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E5%8F%89%E6%A0%91%E4%B8%AD%E5%92%8C%E4%B8%BA%E6%9F%90%E4%B8%80%E5%80%BC%E7%9A%84%E8%B7%AF%E5%BE%84.py)<br>
直接思路:利用递归实现回溯遍历，设置两个列表result和tmp来存放总的答案和遍历到的路径。遍历树的方法选用先序遍历，将遍历到的路径（结点的值）存入tmp列表中，如果一个递归结束，则将tmp的最后一个元素删除，如果判断出已经到达了叶子节点而且路径的值和刚好和所给值一致，则将该tmp列表深拷贝后（python和java只有引用，如果没有深拷贝的话，会导致后面改变tmp的值的时候，连result里的值也会改变）压入result列表中。最后返回result列表。运行时间20ms,占用内存5752k<br>
7.[二叉搜索树的后序遍历](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86.py)<br>
直接思路:利用递归方法判断根节点左右子树是否为二叉搜索树，判断出当前根节点的左子树的范围后，接下来如果有值比根节点小，则说明这不是一颗二叉搜索树。否则就继续递归其子树是否为二叉搜索树。运行时间17ms,占用内存5744k<br>
8.[树的子结构(java、python双版本代码)](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%A0%91%E7%9A%84%E5%AD%90%E7%BB%93%E6%9E%84.py)<br>
直接思路:通过先序遍历找到第二颗树的根节点的值在第一棵树中的位置，然后写一个判断函数不断判断从这个根开始的子树的值是否相同。若有一个不同，则返回False。运行时间21ms,占用内存5712k<br>
9.[字符串的排列(java、python双版本代码)](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E6%8E%92%E5%88%97.py)<br>
直接思路:使用动态规划法。设f(n)为前n个字符的全排列，则f(n)=对f(n-1)的排列中插入第n个字符，对于长度为m的字符串，有m+1中插入方法。所以通过不断迭代插入，就可以得到f(n)。通过集合去重，然后排序即可得到答案。运行时间25ms,占用内存5752k<br>

****
### 数组：<br>
1.[构建乘积数组](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%9E%84%E5%BB%BA%E4%B9%98%E7%A7%AF%E6%95%B0%E7%BB%84.py)<br>
直接思路:使用双重循环直接实现。外层循环是传入的列表的长度，内层循环是列表中元素的乘积，遇到索引相同的则跳过这次循环。运行时间33ms，占用内存5716K<br>
参考思路:经过分析可以发现，B[i]=C[i]\*D[i],其中C[i]=A[0]\*A[1]*...*A[i-1]，D[i]=A[i+1]*...*A[n],则不难发现C[i]=C[i-1]*A\[i-1\](i=1,2...n),C[0]=1。D[i]=D[i+1]*A\[i+1\](i=0,1...n-1)，D[n]=1。有此规律，直接使用两个for循环计算出C和D数组。运行时间27ms，占用内存5816K<br>
2.[二维数组查找](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E6%9F%A5%E6%89%BE.py)<br>
直接思路：将二维数组每一行当做一个数组。然后分别对其进行对半搜索，搜索到则停。时间复杂度大概为O（nlogm），n为二维数组行数，m为二维数组列数。运行时间221 ms，占用内存5732K<br>
参考答案思路：由于二维数组左下角的元素是这一行的最小元素，同时也是这一列的最大元素，那么从这个位置开始对比，若目标元素大则往右走，若目标元素小则往左走。运行时间205 ms，占用内存5852K<br>
3.[数组中重复的数字](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%95%B0%E7%BB%84%E4%B8%AD%E9%87%8D%E5%A4%8D%E7%9A%84%E6%95%B0%E5%AD%97.py)<br>
直接思路:直接把给进的数字列表当队列，出队一个元素后判断元素是否在队列里，如果在，则表示这个元素重复，返回True，要是队列全部元素都出队了，返回False。运行时间22ms,占用内存5852k<br>
间接思路:因为给定的数组里的数字不会大于数组长度-1，所以对于没有重复元素的数组来说，必定是有0\~数组长度-1的数在数组里。所以从下标0开始，将里面的元素和这个元素下标的值进行交换，直到遇见相等的时候表示这个元素重复了。否则就一直交换，直到下标和这个下标对应的数组元素相等时，再对下一个下标重复此操作。如果最后操作完了所有下标，则返回False。运行时间21ms，占用内存5732k<br>
4.[圆圈中最后剩下的数](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%9C%86%E5%9C%88%E4%B8%AD%E6%9C%80%E5%90%8E%E5%89%A9%E4%B8%8B%E7%9A%84%E6%95%B0.py)<br>
直接思路:第一次报数的时候，去掉的是下标为(m-1)%n的小朋友。第二次报数的时候，去掉的是((m-1)%n+m-1)%(n-1)下标的小朋友。所以，易得，设第n次报数去掉的小朋友下标为f\[n\]。则易知f\[1\]=(m-1)%n，f\[2\]=(f\[1\]+m-1)%(n-2)......f\[n-2\]=(f\[n-3\]+m-1)%2。所以，直接用一个列表存储0\~n-1代表n个小朋友。每k次去掉下标为f\[k\]的元素。这样，等到列表只剩1个元素的时候，那个就是剩下来的小朋友。运行时间23ms，占用内存5708k<br>
5.[数组中只出现一次的数字](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%95%B0%E7%BB%84%E4%B8%AD%E5%8F%AA%E5%87%BA%E7%8E%B0%E4%B8%80%E6%AC%A1%E7%9A%84%E6%95%B0%E5%AD%97.py)<br>
直接思路:对列表进行出栈pop操作，然后判断若这个元素存在于列表中，则直接remove这个元素。否则将其加入答案列表，若答案列表中元素有两个，则返回答案列表。运行时间28ms,占用内存5644k<br>
改进思路:由于remove操作的时间复杂度依然会是O(n)，所以多用一个字典存储出栈后的元素，出栈元素不存在于字典的键中，则创建一个这个元素的键，并将其值设为1。判断出栈元素是否在列表中，若存在，则对应键的值+1，否则判断该键对应的值是否为1，若为1则存入答案列表，若答案列表长度是2，直接返回答案列表。运行时间21ms,占用内存5732k<br>
6.[连续子数组的最大和](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E8%BF%9E%E7%BB%AD%E5%AD%90%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E5%A4%A7%E5%92%8C.py)<br>
直接思路:遍历数组所有数，每一个再嵌套循环遍历他后面的数的和，并将所有的和存入列表中，最后返回列表中的最大值。运行时间18ms,占用内存5740k<br>
间接思路:动态规划法。设结尾是第i个元素的最长连续子数组最大值为dp\[i\]，则dp\[i\]=max{dp\[i-1\]+array\[i-1\],array\[i-1\]}，因为在数组array中第i个元素是array\[i-1\]。所以从dp\[0\]=0开始遍历到最后。并且最好每次都判断出dp几最大，然后返回最大值。运行时间18ms,占用内存5748k<br>

### 树：<br>
1.[二叉树的深度](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%B7%B1%E5%BA%A6.py)<br>
直接思路:递归把每个子树的高度都算出来，递归停止条件是空树，递归返回是max{左子树高度，右子树高度}+1(当前层)。运行时间23ms,占用内存5752K。<br>
参考思路:或者借助队列使用层次遍历方法，在开始时记录队列长度，然后将这个长度的个数的元素依次出队列，出队时如果此结点还有左右子树，那么将其左右子树入队。在队列长度个元素出队之后，树的高度+1。运行时间46ms,占用内存5736K<br>
2.[二叉树的镜像](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%95%9C%E5%83%8F.py)<br>
直接思路:使用递归方法不断交换节点的左右子树。运行时间22ms,占用内存5876K。<br>
间接思路:消去递归，使用堆栈，将根节点压入栈中，然后开始循环：若栈不空，出栈一个元素，并交换其左右节点，然后再将其左右节点入栈。否则结束。运行时间21ms，占用内存5736K。<br>
3.[重建二叉树](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E9%87%8D%E5%BB%BA%E4%BA%8C%E5%8F%89%E6%A0%91.py)<br>
直接思路:先序-》第一个是根节点-》中序中寻找到这个根节点，然后将左右切分，左边的结点个数就是根节点左子树的结点个数。去先序接着根找依次这个个数的片段，找到后，又第一个是根节点，以此类推。运行时间66ms，占用内存5984K<br>
4.[把二叉树打印成多行](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%8A%8A%E4%BA%8C%E5%8F%89%E6%A0%91%E6%89%93%E5%8D%B0%E6%88%90%E5%A4%9A%E8%A1%8C.py)<br>
直接思路:用队列和计数器解决，当计数器为0时，说明要开始新的一层了，将计数器置为当前队列长度，每出队一个元素，计数器减一。然后若出队结点的左右子树存在，则将其入队。不断循环这个过程，直到队列为空结束。运行时间30ms,占用内存5832k<br>
间接思路:将直接思路中的计数器用while循环代替优化。然后发现这其实是Bfs的变例。运行时间22ms，占用内存5728k<br>
5.[二叉树的下一个结点](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E4%B8%8B%E4%B8%80%E4%B8%AA%E7%BB%93%E7%82%B9.py)<br>
直接思路:首先将所给结点不断找父节点，直到找到根节点，然后对根节点使用递归中序遍历，然后将中序遍历的结果保存，然后返回定结点的下一个结点就好了。<br>
6.[平衡二叉树](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.py)<br>
直接思路:先用递归写一个获得树高度的函数，然后遍历所有节点，判断其左右子树高度差的绝对值是否大于1，如果大于1则不是二叉平衡树，所有节点遍历完了以后还没返回False，就说明是二叉平衡树。运行时间24ms,占用内存5876k<br>
改进思路:遍历节点的时候可以使用后序遍历法，这样先判断子树满不满足二叉平衡树的条件，如果满足，则继续遍历，否则直接返回False，不需要再判断其根节点了。运行时间25ms,占用内存5636k<br>
7.[二叉搜索树与双向链表](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%8E%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8.py)<br>
直接思路:中序遍历整颗树，将结点存入列表中。然后整个列表是有序的，直接把列表遍历一遍从头到尾连起来就成了有序的双向链表。运行时间27ms，占用内存5752k<br>
8.[二叉搜索树的第k个结点(java、python双版本代码)](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E7%AC%ACk%E4%B8%AA%E7%BB%93%E7%82%B9.py)<br>
直接思路:使用中序遍历将二叉搜索树遍历完了以后得到的列表就是一个有序的列表，只需要取出第k个元素就为结果。运行时间34ms,占用内存5744k<br>
间接思路:但是我们其实只需要第k的结点而已，直接思路的方法却存了一堆没用的结点。所以在使用中序遍历的时候，不将遍历结果存储下来，设置一个计数器，当计数器达到了k的时候，将那个元素返回。运行时间19ms,占用内存5624k<br>
9.[二叉树中和为某一值的路径(java、python双版本代码)](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E5%8F%89%E6%A0%91%E4%B8%AD%E5%92%8C%E4%B8%BA%E6%9F%90%E4%B8%80%E5%80%BC%E7%9A%84%E8%B7%AF%E5%BE%84.py)<br>
直接思路:利用递归实现回溯遍历，设置两个列表result和tmp来存放总的答案和遍历到的路径。遍历树的方法选用先序遍历，将遍历到的路径（结点的值）存入tmp列表中，如果一个递归结束，则将tmp的最后一个元素删除，如果判断出已经到达了叶子节点而且路径的值和刚好和所给值一致，则将该tmp列表深拷贝后（python和java只有引用，如果没有深拷贝的话，会导致后面改变tmp的值的时候，连result里的值也会改变）压入result列表中。最后返回result列表。运行时间20ms,占用内存5752k<br>
10.[二叉搜索树的后序遍历](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86.py)<br>
直接思路:利用递归方法判断根节点左右子树是否为二叉搜索树，判断出当前根节点的左子树的范围后，接下来如果有值比根节点小，则说明这不是一颗二叉搜索树。否则就继续递归其子树是否为二叉搜索树。运行时间17ms,占用内存5744k<br>
11.[树的子结构(java、python双版本代码)](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%A0%91%E7%9A%84%E5%AD%90%E7%BB%93%E6%9E%84.py)<br>
直接思路:通过先序遍历找到第二颗树的根节点的值在第一棵树中的位置，然后写一个判断函数不断判断从这个根开始的子树的值是否相同。若有一个不同，则返回False。运行时间21ms,占用内存5712k<br>

### 字符串：<br>
1.[替换空格](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%9B%BF%E6%8D%A2%E7%A9%BA%E6%A0%BC.py)<br>
直接思路:将字符串以" "为分割点分割。然后再用"20%"组合起来。运行时间32 ms，占用内存5724K<br>
参考思路:直接使用replace方法将" "替换成"20%"。运行时间23 ms，占用内存5752K<br>
不使用函数自己写的思路:遍历一遍字符串，同时生成一个新的字符串，遍历到空格的时候生成字符串的时候生成"%20"。运行时间24ms，占用内存5860K<br>
2.[表示数值的字符串](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E8%A1%A8%E7%A4%BA%E6%95%B0%E5%80%BC%E7%9A%84%E5%AD%97%E7%AC%A6%E4%B8%B2.py)<br>
直接思路:没什么花里胡哨的，直接使用正则匹配，若正则匹配后的结果和原来的结果一样，则返回True，否则返回False。运行时间22ms,占用内存5720k<br>
3.[左旋字符串](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%B7%A6%E6%97%8B%E5%AD%97%E7%AC%A6%E4%B8%B2.py)<br>
直接思路:使用队列，将字符串的字符存入队列中，然后循环n次，出队入队。运行时间32ms,占用内存5752k<br>
间接思路:直接使用字符串切片操作，将字符串切成\[0:n\]的部分和\[n:end\]的部分。然后组合的时候颠倒一下次序。运行时间22ms,占用内存5736k<br>
4.[字符串的排列(java、python双版本代码)](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E6%8E%92%E5%88%97.py)<br>
直接思路:使用动态规划法。设f(n)为前n个字符的全排列，则f(n)=对f(n-1)的排列中插入第n个字符，对于长度为m的字符串，有m+1中插入方法。所以通过不断迭代插入，就可以得到f(n)。通过集合去重，然后排序即可得到答案。运行时间25ms,占用内存5752k<br>

### 数学：<br>
1.[变态台阶跳](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%8F%98%E6%80%81%E8%B7%B3%E5%8F%B0%E9%98%B6.py)<br>
直接思路:通过数学归纳法可以得到n台阶有的跳法为2^(n-1)。则可以直接得到结果。运行时间32 ms，占用内存5840K。<br>
参考思路:设n级台阶能够有的跳法数为f[n]，则很显然f[n]=f[n-1]+f[n-2]+...+f[0]（上一层在n-1层再跳1层+上一层在n-2层再跳2层...上一层没有再跳n层）。运行时间26ms，占用内存5860K<br>
2.[不用加减乘除运算符做加法](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%B8%8D%E7%94%A8%E5%8A%A0%E5%87%8F%E4%B9%98%E9%99%A4%E5%81%9A%E5%8A%A0%E6%B3%95.py)<br>
直接思路:转换成列表型的二进制，然后用if判断来模拟手算二进制的情况，重点在于要补位。（此方法提交时内存溢出）<br>
参考思路:使用位运算符进行操作，两数异或后在左移一位取得进位。值得注意的是，此方法对于C/JAVA来说即使遇到异号数相加大于0的情况也最终会溢出并计算出正确结果，但是python是没有位数限制的，会不断无限的迭代至负无穷，所以对于此类情况应该反着来计算，并将最后结果取反。运行时间20ms，占用内存5860K<br>
3.[扑克牌顺子](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%89%91%E5%85%8B%E7%89%8C%E9%A1%BA%E5%AD%90.py)<br>
直接思路:首先对列表进行排序，然后遍历到第一个不为0的数的下标i。将flag视为i。然后将下标为i的元素与下标i以后的元素逐个比对，如果有相同元素，直接返回false，如果下标为i的元素与后面的元素的差的绝对值大于等于0以外的数个数，那么flag的值减去超出的部分并重新赋值给flag。如果遍历结束后。flag等于0，则返回True，否则返回False。运行时间23ms,占用内存5752k<br>
改进思路:其实不用这么复杂，无论有多少个0，都必须满足最小的那个非0值减去最大的值的绝对值要小于5就可以了。所以只需要排序后，判断最大的值减最小的值的差是否小于5，若小于5则返回True，否则返回False。运行时间21ms，占用内存5624k<br>
4.[和为S的连续正数序列](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%92%8C%E4%B8%BAS%E7%9A%84%E8%BF%9E%E7%BB%AD%E6%AD%A3%E6%95%B0%E5%BA%8F%E5%88%97.py)<br>
直接思路:用i遍历tsum以内的数字，再嵌套用j遍历i以后到tsum的数字，直到i到j的和大于tsum为止。把i到j的和求出来，同时记录下i到j的数字，如果等于tsum，则这组数字即为一个答案。跳出j遍历的循环。运行时间23ms,占用内存5752k<br>
间接思路:数学法。<br>
由于连续数字的和可以用公式来计算，设首项为x，末项为y，则其和为(x+y)\*(y-x+1)\/2。即y^2+y-x^2+x-2\*tsum=0。则可以计算出y=(-1+sqrt(1-4*(-x^2+x-2\*tsum)))/2。若y为整数，则说明x到y则为答案。所以将x从1到tsum进行遍历，计算y的值，若y为整数，则即为一个答案。运行时间22ms,占用内存5624k<br>
5.[整数中1的出现次数\(从1到n整数出现的次数\)](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%95%B4%E6%95%B0%E4%B8%AD1%E5%87%BA%E7%8E%B0%E7%9A%84%E6%AC%A1%E6%95%B0(%E4%BB%8E1%E5%88%B0n%E6%95%B4%E6%95%B0%E5%87%BA%E7%8E%B0%E7%9A%84%E6%AC%A1%E6%95%B0).py)<br>
直接思路:想总结出数学规律，但是失败了。<br>
间接思路:暴力循环。初始化计数器为0，从1到n开始遍历，每个数通过循环取余的方法判断个、十、百。。。位是否为1，然后每有一个位为1，计数器就加1。最后计数器的值就是答案。运行时间37ms,占用内存5740k<br>
6.[数值的整数次方](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%95%B0%E5%80%BC%E7%9A%84%E6%95%B4%E6%95%B0%E6%AC%A1%E6%96%B9.py)<br>
直接思路:调用pow函数。省时省力。运行时间20ms，占用内存5692k<br>
间接思路:分成幂指数大于0，小于0和等于0的情况，大于0时则直接使用for循环乘幂指数次，小于0时则把数值取倒数，然后再for循环乘幂指数次，等于0则直接返回1。运行时间22ms,占用内存5720k<br>

### 链表：<br>
1.[从尾到头打印链表](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BB%8E%E5%B0%BE%E5%88%B0%E5%A4%B4%E6%89%93%E5%8D%B0%E9%93%BE%E8%A1%A8.py)<br>
直接思路:和链表逆置挺像的，头插法插入列表里。如果没有insert方法的话。用堆栈放进去再弹出来。运行时间30 ms，占用内存5728K<br>
2.[链表中环的入口结点](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%8E%AF%E7%9A%84%E5%85%A5%E5%8F%A3%E7%BB%93%E7%82%B9.py)<br>
直接思路:首先把遍历的结点保存在列表中（最好是哈希表其实，这样更快，但是我没有用哈希表）。然后判断新遍历的结点是否存在于列表中，若存在，则直接返回当前结点。否则当所有结点遍历完毕后返回None。运行时间29ms,占用内存5860k<br>
3.[两个链表的第一个公共结点](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%B8%A4%E4%B8%AA%E9%93%BE%E8%A1%A8%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%85%AC%E5%85%B1%E7%BB%93%E7%82%B9.py)<br>
直接思路:两个循环两个指针，从头开始遍历，然后判断是否两个指针指向的结点是否相同。如果相同则返回任意一个指针，否则继续。遍历结束返回空。运行时间18ms,占用内存5764k<br>
间接思路:由于两个链表长度的和是一样的，所以将两个链表拼接起来。到达相同结点的长度肯定是一样的，那么只需要遍历一次，两个指针跟着移动，如果到底了就拼接起来，否则就继续移动，直到找到相同的结点退出循环，并返回那个结点。如果没有公共结点的话，拼起来长度一样，最终都会到两个None，此时也算是相等的结点，刚好返回None。运行时间18ms,占用内存5752k<br>
4.[合并两个排序的链表](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%8E%92%E5%BA%8F%E7%9A%84%E9%93%BE%E8%A1%A8.py)<br>
直接思路:用两个指针指向两个链表的头，然后新创一个链表，判断指针指向的链表的值哪个小，把小的连到新的链表中去，然后对应的那个指针指向下一个元素，直到有某个链表的指针指向了空为止，然后将另一个链表指针后的所有元素再连在新的链表后面。运行时间19ms，占用内存5624k<br>
间接思路:使用递归的方法来实现上述的思路，可以直接用两个链表不停递归连接。但是效率没有直接思路的高。运行时间22ms，占用内存5688k<br>
5.[反转链表](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.py)<br>
直接思路:头插法，从头到尾遍历单链表，新建一个新的单链表节点，不断将遍历到的节点按头插的形式插入新的链表中，即可完成链表的反转。运行时间19ms,占用内存5624k<br>
6.[链表中倒数第k个结点(java、python双版本代码)](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E9%93%BE%E8%A1%A8%E4%B8%AD%E5%80%92%E6%95%B0%E7%AC%ACk%E4%B8%AA%E7%BB%93%E7%82%B9.py)<br>
直接思路:设计一个大小为k的滑动窗口，将两个距离为k-1的指针p1,p2指向链表中的第1个结点和第k个结点，然后同时移动p1和p2，直到p2.next为空为止，则此时p1所指向的结点即为倒数第k个结点。运行时间26ms，占用内存6520k<br>

### 贪心：<br>
1.[剪绳子](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%89%AA%E7%BB%B3%E5%AD%90.py)<br>
思路：设长度为n的绳子剪成起码两段以上的绳子的乘积最大值为f(n)，则易知f(n)=max{1\*f(n-1),2\*f(n-2),...,(n-1)\*f(1)}。而且f(n)起码会切分成两段，而长度为4以下的绳子再切都不可能比原来大，所以长度4以下的绳子需要分类讨论。而大于5长度的绳子f(1)=1,f(2)=2,f(3)=3,f(4)=4。运行时间33ms,占用内存6120K<br>

### 排序：<br>
1.[数据流中的中位数](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%95%B0%E6%8D%AE%E6%B5%81%E7%9A%84%E4%B8%AD%E4%BD%8D%E6%95%B0.py)<br>
直接思路:每输入一个就排序一次，那么奇数列表的中位数就是中间那个数，偶数列表的中位数就是中间两个数之和。运行时间20ms,占用内存5732K<br>
参考思路:利用最大堆和最小堆来实现，将一个数据流的有序排列看作是两个堆的存储。如\[1,2,3,4,5,6\],那么左边1,2,3存储在最大堆中，右边4,5,6存储在最小堆中。那么很显然这个列表的中位数就是最大堆的堆顶元素和最小堆的堆顶元素之和除以2。而如\[1,2,3,4,5\]，那么左边1,2,3存储在最大堆中，右边4,5存储在最小堆中，此时中位数就是最大堆的堆顶元素。那么只要每次把插入的元素，流走于两个堆之间，找到相应的位置，然后再设法将两个堆的元素个数规范，那么中位数就可容易得出。运行时间28ms,占用内存5720K<br>

### 哈希：<br>
1.[字符流中第一个不重复的字符](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%AD%97%E7%AC%A6%E6%B5%81%E4%B8%AD%E7%AC%AC%E4%B8%80%E4%B8%AA%E4%B8%8D%E9%87%8D%E5%A4%8D%E7%9A%84%E5%AD%97%E7%AC%A6.py)<br>
直接思路:首先创建一个字典，用于记录字符出现的次数。再创建一个列表，用于记录插入的字符。若插入的字符在字典中不存在，则在字典中创建新的字符索引并记录值为1，否则对应索引的记录值加1。最后遍历列表，每个元素对应字典中索引中若有记录值为1的，则直接返回这个元素。若列表遍历完毕还没有返回，则返回#。运行时间21ms，占用内存5732k<br>
2.[和为S的两个数字](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%92%8C%E4%B8%BAS%E7%9A%84%E4%B8%A4%E4%B8%AA%E6%95%B0%E5%AD%97.py)<br>
直接思路:从头开始遍历，遇到和大于给定目标值的则直接break，否则如果和等于目标值，则返回这两个值。因为是从头开始遍历的，所以肯定是乘积最小的那组和。运行时间27ms,占用内存5752k<br>
间接思路:哈希法，由于若A+B=SUM，则B=SUM-A，所以先把列表中的值存入字典，然后通过遍历列表，判断SUM-遍历的值是否在字典中，如果在，则判断其乘积是否小而暂存这两个数。最后返回的两个数肯定是最小的。运行时间22ms,占用内存5948k<br>
3.[数组中出现次数超过一半的数字](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%95%B0%E7%BB%84%E4%B8%AD%E5%87%BA%E7%8E%B0%E6%AC%A1%E6%95%B0%E8%B6%85%E8%BF%87%E4%B8%80%E5%8D%8A%E7%9A%84%E6%95%B0%E5%AD%97.py)<br>
直接思路:哈希法，构建一个哈希表，遍历一遍数组，如果遍历到的元素存在于哈希表，则对应的哈希值+1，并判断此哈希值是否超过了数组长度的一半，如果是则返回此值。若遍历到的元素不存在于哈希表内，则创建对应的哈希键值并赋值为1。遍历完数组后返回0。运行时间18ms，占用内存5728k<br>
间接思路:候选法，由于众数肯定是超过数组中的一半的那个数，所以将数组中两个不相等的元素相互抵消，这样每次最差的结果就是抵消了一个众数和一个非众数，最终保留在数组中的一定是众数。所以创建一个候选人模型，遍历过程中用一个选票值变量cnt记录当前候选数cond所有的次数，当cnt为0的时候，说明该值已经被抵消过了，取当前遍历的这个值重新做候选数，并让其cnt+1。若cnt不为0，则说明候选数当前没有抵消完，判断候选数与当前遍历到的元素是否相等，如果相等则cnt+1，否则就和当前元素抵消掉，cnt-1。最后保留的那个候选数，再判断它在数组中出现次数是否大于数组一半。运行时间18ms,占用内存5796k<br>

### 位运算符：<br>
1.[求1+2+...+n](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%B1%821%2B2...%2Bn.py)<br>
直接思路:使用递归加来代替循环。利用and的短路原理来实现递归的终止。运行时间31ms,占用内存5752k<br>
2.[二进制中1的个数](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E4%BA%8C%E8%BF%9B%E5%88%B6%E4%B8%AD1%E7%9A%84%E4%B8%AA%E6%95%B0.py)<br>
直接思路:正数好办，直接辗转相除法，然后判断每次余数是否等于1，等于1就计数。对于负数，由于剑指上使用的是32位的数，但是python是无限位数的。所以首先把负数变成正数，然后开始辗转相除法，并且每次取余数的时候，要取反码。使用两个标记flag和bin_count记录当前情况，flag=1表示已经解决完补码+1的问题了，剩下的直接判断反码是1还是0就可以了，flag=2表示补码+1的进位还在，此时遇到余数为1要继续进位，直到余数为0或者超32位为止。bin_count用于记录当前是多少位了，少于32位循环将继续下去，并且每次都是余数视为1。运行时间19ms，占用内存5748k<br>
间接思路:发现有val :1101000, val-1: 1100111 那么val & （val-1） : 1100000的规律，那么每次遇到一个1，都可以通过val&val-1的方式去消除那个1。所以只需要在给定的数n不为0且n>=-2147483648(32位的最小值)的时候，不断循环计数+1，n=n&(n-1)。运行时间18ms,占用内存5748k<br>

### 二分搜索：<br>
1.[数字在排序数组中出现的次数](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%95%B0%E5%AD%97%E5%9C%A8%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E5%87%BA%E7%8E%B0%E7%9A%84%E6%AC%A1%E6%95%B0.py)<br>
直接思路:利用一次循环遍历列表，判断相等的目标元素的个数。如果遇到大于目标元素的值，则break。运行时间21ms,占用内存5728k<br>
间接思路:二分搜索法寻找目标元素的边界。上界为使用二分搜索法寻找到第一个大于目标元素值的索引，下界为使用二分搜索法寻找到第一个等于目标元素值的索引，如果目标元素不存在于列表中，则下界肯定只能寻得第一个大于目标元素值的索引。最终的目标元素出现次数为上界减去下界。运行时间17ms,占用内存5752k<br>
2.[旋转数组的最小数字](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%97%8B%E8%BD%AC%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E5%B0%8F%E6%95%B0%E5%AD%97.py)<br>
直接思路:由于旋转后的数组必然出现断崖式的值变化，而且在出现变化前都是单调不减的，所以只需要遍历判断前一个元素比后一个元素大的时候返回那个后一个元素。然后如果遍历完整个数组都不存在前一个元素比后一个元素大，则返回数组\[0\]。运行时间482ms,占用内存5748k，在LeetCode中执行时间44ms，击败45.82%用户，占用内存13.9MB，击败9.23%的用户<br>
间接思路:利用二分搜索的方法对数组进行搜索，首先要解决的就是比较元素的选取问题，这里我们取中间值，然后与两个边界值进行比较，如果中间值比左边界的元素大，则左边界变成mid+1，因为说明前面还是增，否则就判断中间值元素是否比右边界小，如果比右边界小，说明右边区域是单增的，所以右边界变为中间值，如果既不比左边界值大，又不比右边界小，则左边界+1。运行时间513ms,占用内存5748k,在LeetCode中执行时间32ms，击败96.9%用户，内存消耗13.8MB，击败24.62%用户。<br>

### 动态规划法：<br>
1.[连续子数组的最大和](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E8%BF%9E%E7%BB%AD%E5%AD%90%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E5%A4%A7%E5%92%8C.py)<br>
直接思路:遍历数组所有数，每一个再嵌套循环遍历他后面的数的和，并将所有的和存入列表中，最后返回列表中的最大值。运行时间18ms,占用内存5740k<br>
间接思路:动态规划法。设结尾是第i个元素的最长连续子数组最大值为dp\[i\]，则dp\[i\]=max{dp\[i-1\]+array\[i-1\],array\[i-1\]}，因为在数组array中第i个元素是array\[i-1\]。所以从dp\[0\]=0开始遍历到最后。并且最好每次都判断出dp几最大，然后返回最大值。运行时间18ms,占用内存5748k<br>
2.[矩形覆盖](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E7%9F%A9%E5%BD%A2%E8%A6%86%E7%9B%96.py)<br>
直接思路：通过人工计算前4个矩形的覆盖方法数可得，假设用n个2\*1的矩形覆盖一个2\*n的矩形的方法数为f\[n\]，则f\[n\]=f\[n-1\]+f\[n-2\]。那么根据递推的规则，很容易想到动态规划法，使用动态规划法进行递推计算，得到f\[n\]。运行时间26ms,占用内存5684k<br>
3.[跳台阶](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E8%B7%B3%E5%8F%B0%E9%98%B6.py)<br>
直接思路：很容易就能想到，台阶为n的情况下，可以是台阶n-1的基础上跳1台阶跳上来，也可以是台阶n-2的基础上跳2台阶跳上来，所以很显然假设跳n台阶的跳法为f\[n\]，且f\[n\]=f\[n-1\]+f\[n-2\]。可以利用动态规划法递推计算出来。运行时间18ms,占用内存5744k<br>
4.[斐波那契数列](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97.py)<br>
直接思路：动态规划法的例子，本身斐波那契数列就是递推式，直接递推计算即可。运行时间16ms,占用内存5744k<br>
5.[字符串的排列(java、python双版本代码)](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E6%8E%92%E5%88%97.py)<br>
直接思路:使用动态规划法。设f(n)为前n个字符的全排列，则f(n)=对f(n-1)的排列中插入第n个字符，对于长度为m的字符串，有m+1中插入方法。所以通过不断迭代插入，就可以得到f(n)。通过集合去重，然后排序即可得到答案。运行时间25ms,占用内存5752k<br>

### 场景模拟法：<br>
1.[栈的压入、弹出序列](https://github.com/IPostYellow/SwordTarget-OFFER/blob/master/%E6%A0%88%E7%9A%84%E5%8E%8B%E5%85%A5%E3%80%81%E5%BC%B9%E5%87%BA%E5%BA%8F%E5%88%97.py)<br>
直接思路:本来想着找出什么规律，但是根本没有发现规律。<br>
间接思路:模拟法，根据输出的序列，模拟入栈，如果最终可以成功将栈清空，则说明输出序列可行，否则不可行。具体做法是：利用两个指针p1,p2分别指向输入和输出的序列首端。直到两个指针超界前循环判断p1所指元素是否等于p2所指元素，如果不等，则将p1指向元素压入栈中，并且p1指向下一个元素。如果相等，则说明入栈马上出栈，则直接p1和p2指向下一个元素，此时直到p2指向元素不等于栈顶元素，循环出栈栈顶元素。最终全部循环结束后，若栈为空，则说明输出序列可能，返回True，否则返回False。运行时间19ms，占用内存5752k<br>
