package org.pcsiszar.corsair.attribute;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.ToString;

@RequiredArgsConstructor
@Getter
@EqualsAndHashCode
@ToString
public class AttributePair {
  private Attribute left;
  private Attribute right;
}
