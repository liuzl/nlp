licenses(["notice"])  #  BSD/MIT-like license

cc_library(
    name = "thulaclib",
    hdrs = glob(["src/*.h"]),
    includes = ["."],
    visibility = ["//visibility:public"],
)

cc_binary(
    name = "train_c",
    srcs = ["src/train_c.cc",],
    deps = [":thulaclib",],
)

cc_binary(
    name = "thulac",
    srcs = ["src/thulac.cc",],
    deps = [":thulaclib",],
)
