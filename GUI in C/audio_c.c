#include<stdio.h>
#include<stdlib.h>

typedef struct header
{
    char chunk_id[4];
    int chunk_size;
    char format[4];
    char subchunk1_id[4];
    int subchunk1_size;
    short int num_channels;
    int sample_rate;
    int byte_rate;
    short int block_align;
    short int bits_per_sample;
    short int extra_param_size;
    char subchunk2_id[4];
    int subchunk2_size;
}header;

typedef struct header* header_p;

void scale_wav_file(char* input, float factor, int is_8bit)
{
    FILE * infile = fopen(input, "rb");
    FILE * outfile = fopen("audio.wav", "wb");

    int BUFSIZE = 4000, i, MAX_8BIT_AMP = 255, MAX_16BIT_AMP = 32678;

    // used for processing 8-bit file

    unsigned char inbuff8[BUFSIZE], outbuff8[BUFSIZE];

    // used for processing 16-bit file
    short int inbuff16[BUFSIZE], outbuff16[BUFSIZE];
    
}