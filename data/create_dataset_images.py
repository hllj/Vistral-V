if args.stage == "all" or args.stage == 'pretrain':
    # Download llava pretrain dataset
    hf_hub_download(repo_id="Vi-VLM/Vista", filename="images/llava/images.zip", local_dir=local_dir, repo_type="dataset")

    # Download SAM pretrain dataset
    sam_images_parts = [
        "images/sam/images_part_aa",
        "images/sam/images_part_ab",
        "images/sam/images_part_ac",
        "images/sam/images_part_ad",
        "images/sam/images_part_ae",
        "images/sam/images_part_af",
        "images/sam/images_part_ag",
        "images/sam/images_part_ah",
        "images/sam/images_part_ai",
        "images/sam/images_part_aj",
        "images/sam/images_part_ak",
        "images/sam/images_part_al",
        "images/sam/images_part_am"
    ]
    for filename in sam_images_parts:
        hf_hub_download(repo_id="Vi-VLM/Vista", filename=filename, local_dir=local_dir, repo_type="dataset")

    # Download share_textvqa dataset
    hf_hub_download(repo_id="Vi-VLM/Vista", filename="images/share_textvqa/images.zip", local_dir=local_dir, repo_type="dataset")

    # Download web-landmark dataset
    hf_hub_download(repo_id="Vi-VLM/Vista", filename="images/web-landmark/images.zip", local_dir=local_dir, repo_type="dataset")

    # Download web-celebrity dataset
    hf_hub_download(repo_id="Vi-VLM/Vista", filename="images/web-celebrity/images.zip", local_dir=local_dir, repo_type="dataset")

    # Download wikiart dataset
    hf_hub_download(repo_id="Vi-VLM/Vista", filename="images/wikiart/images.zip", local_dir=local_dir, repo_type="dataset")
    
    # Download WIT dataset
    wit_images_parts = [
        "images_part_aa", "images_part_ab", "images_part_ac", "images_part_ad", "images_part_ae",
        "images_part_af", "images_part_ag", "images_part_ah", "images_part_ai", "images_part_aj",
        "images_part_ak", "images_part_al", "images_part_am", "images_part_an", "images_part_ao",
        "images_part_ap", "images_part_aq", "images_part_ar", "images_part_as", "images_part_at",
        "images_part_au", "images_part_av", "images_part_aw", "images_part_ax", "images_part_ay",
        "images_part_az", "images_part_ba", "images_part_bb", "images_part_bc", "images_part_bd",
        "images_part_be", "images_part_bf", "images_part_bg", "images_part_bh", "images_part_bi",
        "images_part_bj", "images_part_bk", "images_part_bl", "images_part_bm", "images_part_bn",
        "images_part_bo", "images_part_bp", "images_part_bq", "images_part_br", "images_part_bs",
        "images_part_bt", "images_part_bu", "images_part_bv", "images_part_bw", "images_part_bx",
        "images_part_by", "images_part_bz", "images_part_ca", "images_part_cb", "images_part_cc",
        "images_part_cd", "images_part_ce", "images_part_cf", "images_part_cg", "images_part_ch",
        "images_part_ci", "images_part_cj", "images_part_ck", "images_part_cl", "images_part_cm",
        "images_part_cn", "images_part_co", "images_part_cp", "images_part_cq", "images_part_cr",
        "images_part_cs", "images_part_ct", "images_part_cu", "images_part_cv", "images_part_cw",
        "images_part_cx", "images_part_cy", "images_part_cz"
    ]
    for filename in wit_images_parts:
        hf_hub_download(repo_id="Vi-VLM/Vista", filename=filename, local_dir=local_dir, repo_type="dataset")
