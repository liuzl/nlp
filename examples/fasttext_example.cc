#include "fasttext.h"

int main(int argc, char* argv[]) {
    utils::initTables();
    if (argc < 2) {
        exit(EXIT_FAILURE);
    }
    utils::freeTables();
    return 0;
}
