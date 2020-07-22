---
layout: default
title: Publications
permalink: publications.html
---


  <!-- Nav tabs -->
  <ul class="nav nav-tabs nav-fill" role="tablist">
    <li class="nav-item"><a class="nav-link active" href="#publications" aria-controls="cookbooks" role="tab" data-toggle="tab">OpenMBEE Publications</a></li>
    <li class="nav-item"><a class="nav-link" href="#com_publications" aria-controls="mdk" role="tab" data-toggle="tab">Community Publications</a></li>
  </ul>

  <div class="tab-content">
    <div role="tabpanel" class="tab-pane active" id="publications">
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
    </div>

    <div role="tabpanel" class="tab-pane" id="com_publications">
        <div class="table-responsive">
        <table class="table table-hover w-auto">
          <thead class="thead-dark">
            <tr>
              <th scope="col"></th>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Organization</th>
            </tr>
          </thead>
  
          <tbody>
          {% for pub in site.data.com_publications %}
            <tr>
              <th scope="row"></th>
              {% if pub.Links %}
                <td><a href="{{pub.Links}}" target="_blank">{{pub.Title}}</a></td>
              {% else %}
                <td>{{pub.Title}}</td>
              {% endif %}
              <td>{{pub.Author}}</td>
              <td>{{pub.Organization}}</td>
            </tr>
           {% endfor %}
          </tbody>
        </table>
    </div>
    </div>

  </div>