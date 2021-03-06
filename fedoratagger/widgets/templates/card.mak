<div class="${w.css_class}">
  <div class="content">
    <div class="clear"></div>
    <div class="package_header">
      <div class="title">
        % if w.package.icon:
          <div class="icon"><img src="${w.package.icon}"/></div>
        % endif
        <div><h2>${w.package.name}</h2></div>
        <div class="summary">
          % if w.package.summary:
            ${w.package.summary}
          % else:
            ${w.package.xapian_summary}
          % endif
        </div>
      </div>
        <div class="details">
		<a href="javascript:more_details('${w.package.name}');">More details...</a>
        </div>
        <div class="clear"></div>
    </div>
    <div class="clear"></div>
    <div class="question">
      % if w.tags:
      Do these tags match this package?
     % endif
    </div>
    <div class="clear"></div>
    <div class="tags">
      <ul>
% for tag in w.tags:
          ${tag.display() | n}
% endfor
      </ul>
    </div>
    <div class="clear"></div>
% if w.not_anonymous:
	<div class="new">
		<div class="plus" onclick="javascript:$('#add_dialog').dialog('open');"></div>Add a new tag.
	</div>
% endif
  </div>
</div>
