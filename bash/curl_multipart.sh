#!/bin/bash

# Send multipart/form-data with a mp3 file
curl -F "audio_file=@./tts_test.mp3" http://test.com

# Send multipart/form-data with multiple files
curl -F "file1=@/upload/file1/path" -F "file2=@/upload/file2/path" http://file.testApi.com

# Send multipart/form-data with multiple files - file variable is an array
curl -F "file[]=@/upload/file1/path" -F "file[]=@/upload/file2/path" http://file.testApi.com
