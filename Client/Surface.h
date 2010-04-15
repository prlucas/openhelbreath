#ifndef SURFACE_H
#define SURFACE_H

#include <SDL.h>
#include <SDL_image.h>
#include <string>

class Surface
{
public:
	Surface();

	static SDL_Surface *LoadFromImage(const std::string &FileName);

	static SDL_Surface *CreateSurface(int W, int H, int R, int G, int B, int Alpha);

	static bool Draw(SDL_Surface *Dest, SDL_Surface *Src, int X, int Y);

	static bool Draw(SDL_Surface *Dest, SDL_Surface *Src, int X, int Y, int X2, int Y2, int W, int H);

	static bool SetTransparent(SDL_Surface *Dest, int R, int G, int B);

	static Uint32 GetPixel32(SDL_Surface *Src, int X, int Y);

	static void ReplaceColor(SDL_Surface *Dest, Uint32 A, Uint32 B);
};

#endif // SURFACE_H
