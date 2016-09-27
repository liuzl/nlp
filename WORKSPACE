maven_jar(
    name = "edu_stanford_nlp_stanford_corenlp",
    artifact = "edu.stanford.nlp:stanford-corenlp:3.6.0",
)

maven_jar(
    name = "org_slf4j_slf4j_api",
    artifact = "org.slf4j:slf4j-api:1.7.21",
)

new_git_repository(
    name = "thulac_git",
    commit = "33f1bd859c36b36368e4261f344f2296f297c12f",
    remote = "https://github.com/thunlp/THULAC.git",
    build_file = "third_party/thulac/BUILD",
)

new_git_repository(
    name = "com_github_facebookresearch_fasttext",
    commit = "f2aa520563f0c67ad980a5caacc1c9728b3af099",
    remote = "https://github.com/facebookresearch/fastText.git",
    build_file = "third_party/fasttext/BUILD",
)
