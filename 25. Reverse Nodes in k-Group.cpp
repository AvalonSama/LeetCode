#include <bits/stdc++.h>

using namespace std;
//  Definition for singly-linked list.
struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
  };
 
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        int length = 0;
        ListNode* temp = head;
        while(temp!=NULL)
        {
            temp=temp->next;
            length++;
        }
        int count = 0;
        ListNode* pre = NULL;
        ListNode* now = head;
        ListNode* next = now->next;
        bool flag = false;
        while(length-count>=k)
        {
            count+=k;
            int temp_count=0;
            ListNode* tag = now;
            while(temp_count<k)
            {
                temp_count++;
                now->next = pre;
                pre = now;
                now = next;
                next = next->next;
            }
            tag->next = now;
            if(flag == false)
            {
                flag = true;
                head = pre;
            }
        }
        return head;
    }
};

void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}

void trimRightTrailingSpaces(string &input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}

vector<int> stringToIntegerVector(string input) {
    vector<int> output;
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    stringstream ss;
    ss.str(input);
    string item;
    char delim = ',';
    while (getline(ss, item, delim)) {
        output.push_back(stoi(item));
    }
    return output;
}

ListNode* stringToListNode(string input) {
    // Generate list from the input
    vector<int> list = stringToIntegerVector(input);

    // Now convert that list into linked list
    ListNode* dummyRoot = new ListNode(0);
    ListNode* ptr = dummyRoot;
    for(int item : list) {
        ptr->next = new ListNode(item);
        ptr = ptr->next;
    }
    ptr = dummyRoot->next;
    delete dummyRoot;
    return ptr;
}

int stringToInteger(string input) {
    return stoi(input);
}

string listNodeToString(ListNode* node) {
    if (node == nullptr) {
        return "[]";
    }

    string result;
    while (node) {
        result += to_string(node->val) + ", ";
        node = node->next;
    }
    return "[" + result.substr(0, result.length() - 2) + "]";
}

int main() {
    string line;
    while (getline(cin, line)) {
        ListNode* head = stringToListNode(line);
        getline(cin, line);
        int k = stringToInteger(line);
        
        ListNode* ret = Solution().reverseKGroup(head, k);

        string out = listNodeToString(ret);
        cout << out << endl;
    }
    return 0;
}