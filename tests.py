from LithoConverter import BinVectorMarker
from LithoConverter import gen_similar_word_freq_csv,open_csv_df,gen_eng_compressed_csv,gen_llm_word_def_csv
from LithoConverter import gen_csvs
import os 


if __name__ == "__main__":
    CWD             = os.getcwd()
    BRIT_DF_PATH    = os.path.join(CWD,"British Columbia","Lithogeochemical","lithogeochem_data.csv")
  
    brit_df       = open_csv_df(BRIT_DF_PATH)
    





    df:pd.Series = pd.concat([
                    brit_df['Sample_Desc'], 
                    # usgs_df['ADDL_ATTR'],
                    # usgs_df['SPEC_NAME'],
                    # usgs_df["XNDRYCLASS"],
                    # sarig_df['feature'],
                    # ontario_df['ROCK'],
                    # ontario_df['ROCK.1'],
                    # ontario_df['ROCK.2']
                    ],axis=0)


    print(df.shape)
    csv_out_folder = 'LITHO_CSVS'


    if not(os.path.exists(csv_out_folder)):
        gen_csvs(df,out_dir=csv_out_folder)
    


    
    sim_key_word_csv_path = os.path.join(CWD,csv_out_folder,"similar_keywords_compressed_freq.csv")
    word_def_csv_path     = os.path.join(CWD,csv_out_folder,"word_def.csv")


    BIN_VEC_MARKER = BinVectorMarker(sim_key_word_csv_path,word_def_csv_path)


    bin_vecs= BIN_VEC_MARKER.gen_bin_vecs(df).apply(lambda x: ','.join(map(str, x)))


    bin_vec_df = pd.concat([df,bin_vecs],keys=['Sample_Descr','Bin_Vec'],axis=1)

    bin_vec_df.to_csv("bin_vec.csv")



    
    sim_key_word_csv_path = os.path.join(CWD,csv_out_folder,"similar_keywords_compressed_freq.csv")
    word_def_csv_path     = os.path.join(CWD,csv_out_folder,"word_def.csv")


    BIN_VEC_MARKER = BinVectorMarker(sim_key_word_csv_path,word_def_csv_path)


    bin_vecs= BIN_VEC_MARKER.gen_bin_vecs(df).apply(lambda x: ','.join(map(str, x)))


    bin_vec_df = pd.concat([df,bin_vecs],keys=['Sample_Descr','Bin_Vec'],axis=1)

    bin_vec_df.to_csv("bin_vec.csv")

