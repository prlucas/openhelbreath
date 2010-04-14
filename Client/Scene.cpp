#include "Scene.h"

Scene::Scene()
{

}

void Scene::OnLoop()
{

}

void Scene::Draw(SDL_Surface *Dest)
{
	DrawVersion(Dest);
}

inline void Scene::DrawVersion(SDL_Surface *Dest) const
{
	char Ver[20];
	sprintf(Ver, "V%d.%d", DEF_LOWERVERSION, DEF_UPPERVERSION);
	Font::PutTextSprF(Dest, 14, 463, Ver);
}




