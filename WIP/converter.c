#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to convert file from one format to another
void convert_file(char* input_filename, char* output_filename) {
    // Open input file for reading in binary mode
    FILE* input_file = fopen(input_filename, "rb");
    if (!input_file) {
        printf("Error: Cannot open input file %s\n", input_filename);
        return;
    }
    
    // Open output file for writing in binary mode
    FILE* output_file = fopen(output_filename, "wb");
    if (!output_file) {
        printf("Error: Cannot open output file %s\n", output_filename);
        return;
    }
    
    // Read input file into memory
    fseek(input_file, 0, SEEK_END);
    long input_file_size = ftell(input_file);
    rewind(input_file);
    char* input_buffer = (char*)malloc(input_file_size);
    fread(input_buffer, input_file_size, 1, input_file);
    
    // Write output file
    fwrite(input_buffer, input_file_size, 1, output_file);
    
    // Clean up
    free(input_buffer);
    fclose(input_file);
    fclose(output_file);
    
    printf("Conversion successful: %s -> %s\n", input_filename, output_filename);
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        printf("Usage: %s <input_file> <output_file>\n", argv[0]);
        return 1;
    }
    
    char* input_filename = argv[1];
    char* output_filename = argv[2];
    
    convert_file(input_filename, output_filename);
    
    return 0;
}
