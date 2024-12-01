#include <stdio.h>
#include <gvc.h>

int main(){
	GVC_t *gvc;
	Agraph_t *G;

	gvc = gvContext(); /* library function */
	G = createGraph ();
	agclose (G); /* library function */
	gvFreeContext(gvc);

	return 0;
}
