#include ‹cerrno>
#include < cstdlib> #include < cstdint> #include <cstring> #include ‹stream›
#include < iostream›
struct ImageHeader {
uint16_t width;
uint16_t height;
char bytes_per_pixel;
char checksum (32);
char *generate_checksum(char *filename, char *data, size_t size) (
// generates a mds checksum of image data
chan *command, *hash_filename, *checksum;
FILE *P, *hashfp; asprintf(Shash_filename, "Xs. tmp'
, filename);
asprintf(&connand, "edSsun %s", hash_filenane);
hashfp = fopen (hash_filename, w);
farite(data, 1, size, hashfp);
I
fclose(hashfp);
P= popen (connand, "r*):
checksun = (char*)malloc(33);
fgets (checksun, 33, p); checksun(32] • *10'; free (hash_filenane);
free (conmand) ;
void save image (chan *filename, Imagetteader *header, char *data, size_t size) ( char output _filenane[strien(filenane) + 4); sprintf(output filename, std: :ofstrean outfile;
*%.new, fIlenane);
outfile.open(output_filename,
outfile.write((char*)header,
std: slos: =binary
std::los: sout);
outfile unite(data, size);
sizeof (Imagetteader));

outfile.close();
void apply_filter(unsigned char *line, uinti6_t size, float fade) ( unsigned int r, g, b, a, gray;
fade = 1 - fade;
for (int i = 0; i < size; i += 4) (
r = line[1];
g = line[i + 1];
b = line[i + 2];
gray = ((r + g + b) / 3) -* fade;
line[i] = gray;
line[i + 1] = gray;
line[i + 2] = gray;
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
int process_image(char. *filename) i
Imageheader header; std: ifstrean infile;
infile. open (filename, std: ios: abinary | std::o]:in);
infile.read((char*)äheader, sizeof (Sheader));
if (header.bytes_per_pixel < 4) (
std: cerr « "unsupported image format, must be ROBA* infile.close);
« stds sendi;
recurn false;
61
62
wint1s_t Linesize = header.sidth • header.bytes _per_pixel;
