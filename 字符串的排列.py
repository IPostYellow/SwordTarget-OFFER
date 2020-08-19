class Solution:#递归法 20ms,5752k
    def perm(self,pos,ss,ret):
        ss=list(ss)
        if pos+1==len(ss):
            ret.append(''.join(ss))
            return None
        for i in range(pos,len(ss)):
            tmp=ss[pos]
            ss[pos]=ss[i]
            ss[i]=tmp
            self.perm(pos+1,ss,ret)
            tmp=ss[pos] #回溯换回来
            ss[pos]=ss[i]
            ss[i]=tmp
    def Permutation(self, ss):
        # write code here
        if ss == "":
            return []
        if len(ss) == 1:
            return [ss]
        ret=[]
        self.perm(0,ss,ret)
        return sorted(list(set(ret)))

S=Solution()
print(S.Permutation('abcd'))

class Solution:#动态规划法 25ms 5752k
    def Inserti(self,ss,i,word):
        A=ss[0:i]
        B=ss[i:]
        return A+word+B
    def Permutation(self, ss):
        # write code here
        if ss=="":
            return []
        if len(ss)==1:
            return[ss]
        curset=[ss[0]]
        for word in ss[1:]:
            size=len(curset)
            while(size!=0):
                tmp=curset.pop(0)
                for i in range(len(tmp)+1):
                    curset.append(self.Inserti(tmp,i, word))
                size-=1
        return sorted(list(set(curset)))

#java 83ms 12264k
# import java.util.ArrayList;
# import java.util.HashSet;
# import java.util.Collections;
#
# public class Solution {
#     public String Inserti(String str,int i,char word){
#         String A=str.substring(0,i);
#         String B=str.substring(i);
#         return A+word+B;
#     }
#     public ArrayList<String> Permutation(String str) {
#        ArrayList<String> result=new ArrayList<String>();
#        if (str.equals("")||(str==null)) return result;
#        if (str.length()==1){
#             result.add(str);
#             return result;
#         }
#         result.add(str.substring(0,1));
#         for (char s:str.substring(1).toCharArray()){
#             int sz=result.size();
#             while (sz>0){
#                 String tmp=result.remove(0);
#                 int i;
#                 for(i=0;i<tmp.length()+1;i++)
#                     result.add(Inserti(tmp,i,s));
#                 sz--;
#             }
#       }
#         HashSet h= new HashSet(result);
#         result.clear();
#         result.addAll(h);
#         Collections.sort(result);
#         return result;
#     }
# }