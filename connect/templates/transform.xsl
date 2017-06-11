<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output encoding="utf-8" indent="yes" method="xml" omit-xml-declaration="no" version="1.0"/>
  <xsl:template match="/">
    <georecords>
      <xsl:apply-templates select="//record"/>
    </georecords>
  </xsl:template>
  <xsl:template match="record">
    <georecord>
      [[FIELDS]]   
    </georecord>
  </xsl:template>
</xsl:stylesheet>