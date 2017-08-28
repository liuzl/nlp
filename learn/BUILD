java_binary(
    name = "nlpseg",
    srcs = [
        "CoreNLPSegment.java",
        "CoreNLP-chinese.properties",
    ],
    main_class = "CoreNLPSegment",
    deps = [
        "@edu_stanford_nlp_stanford_corenlp//jar",
        "@org_slf4j_slf4j_api//jar"
    ],
)

cc_binary(
    name = "jieba_demo",
    srcs = ["jieba_demo.cc",],
    deps = [
        "@com_github_liuzl_cppjieba//:cppjieba"
    ],
    data = [
        "@com_github_liuzl_cppjieba//:dict",
    ],
)

java_binary(
    name = "hanlp-demo",
    srcs = [
        "HanLPDemo.java",
    ],
    main_class = "HanLPDemo",
    deps = [
        "@com_hankcs_hanlp//jar",
    ],
)
