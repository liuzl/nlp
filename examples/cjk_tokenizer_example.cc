#include <iostream>
#include <string>
#include <vector>

#include "cjk-tokenizer.h"

using namespace std;

int main(int argc, char* argv[])
{
    cjk::tokenizer tknzr;
    tknzr.ngram_size = 1;
    //tknzr.max_token_count = 0;
    tknzr.han_conv_method = cjk::HAN_CONV_NONE;

    string line;
    vector<pair<string, unsigned>> token_list;
    vector<pair<string, unsigned>>::iterator it;
    cout << ">";
    while (getline(cin, line)) {
        token_list.clear();
        tknzr.tokenize(line, token_list);
        for (it = token_list.begin(); it != token_list.end(); ++it) {
            cout << it->first << ", " << it->second << endl;
        }
        cout << endl << ">";
    }
    return 0;
}
