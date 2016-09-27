licenses(["notice"])

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "fasttext",
    hdrs = glob(["src/*.h"]),
    srcs = glob(["src/*.cc"]),
    includes = ["src",],
)

cc_binary(
    name = "main",
    deps = [":fasttext",],
)
