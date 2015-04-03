all: nerf_proto_desc.pdf wiring_guide.pdf

nerf_proto_desc.pdf: nerf_proto_desc.tex
	pdflatex nerf_proto_desc.tex

wiring_guide.pdf: wiring_guide.tex
	pdflatex wiring_guide.tex

clean:
	rm -f *.pdf *.log *.aux

.PHONY:
	clean
