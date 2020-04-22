---
layout: default
title: Publications
permalink: publications.html
---


<div class="table-responsive">
<table class="table table-hover w-auto">
  <thead class="thead-dark">
    <tr>
	  <th scope="col"></th>
      <th scope="col">Title</th>
      <th scope="col">Author</th>
      <th scope="col">Location</th>
    </tr>
  </thead>
  
  <tbody>
  {% for pub in site.data.publications %}
    <tr>
      <th scope="row"></th>
      {% if pub.Links %}
        <td><a href="{{pub.Links}}" target="_blank">{{pub.Title}}</a></td>
      {% else %}
        <td>{{pub.Title}}</td>
      {% endif %}
      <td>{{pub.Author}}</td>
      <td>{{pub.Location}}</td>
    </tr>
   {% endfor %}
  </tbody>
</table>
</div>
