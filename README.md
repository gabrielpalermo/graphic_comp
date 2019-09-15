# graphic_comp
Graphic computing projects

**Projective Transformation**
- Input:
  - texture image;
  - base image; and
  - set of destination coordinates.
- Output:
  - base image with mapped texture

- Step by step:
  - from the destination coordinates and texture size, find the projective transformation matrix;
  - solve 12x12 linear system;
  - find the inverse matrix; and
  - apply the reverse projective transformation to base image to find matching texture points, replace pixels.

<div margin-left="10">
  <div>
    <img src="https://raw.githubusercontent.com/gabrielpalermo/graphic_comp/master/img/base.jpg" alt="base_image" title="Base image" width="256" height="144" />
  </div>
  <div>
    <img src="https://raw.githubusercontent.com/gabrielpalermo/graphic_comp/master/img/texture.jpg" alt="texture_image" title="Texure image" width="144" height="144" />
  </div>
  <div>
    <img src="https://raw.githubusercontent.com/gabrielpalermo/graphic_comp/master/img/res2.jpg" alt="result_image" title="Mapped texture on base image" width="256" height="144" />
  </div>
</div>
 
