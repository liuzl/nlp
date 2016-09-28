workspace(name = "com_github_liuzl_nlp")

maven_jar(
    name = "edu_stanford_nlp_stanford_corenlp",
    artifact = "edu.stanford.nlp:stanford-corenlp:3.6.0",
)

maven_jar(
    name = "org_slf4j_slf4j_api",
    artifact = "org.slf4j:slf4j-api:1.7.21",
)

maven_jar(
    name = "com_hankcs_hanlp",
    artifact = "com.hankcs:hanlp:portable-1.2.11",
)

git_repository(
    name = "com_github_liuzl_cppjieba",
    commit = "76356ead3f5909d00fb1a2d57d8e64737d234043",
    remote = "https://github.com/liuzl/cppjieba.git",
)

new_git_repository(
    name = "com_github_facebookresearch_fasttext",
    commit = "f2aa520563f0c67ad980a5caacc1c9728b3af099",
    remote = "https://github.com/facebookresearch/fastText.git",
    build_file = "third_party/fasttext/BUILD",
)

git_repository(
    name = "com_github_liuzl_cjk_tokenizer",
    commit = "f4d3d81e135d3e8c256fc307a164676004ec2296",
    remote = "https://github.com/liuzl/cjk-tokenizer.git",
)
